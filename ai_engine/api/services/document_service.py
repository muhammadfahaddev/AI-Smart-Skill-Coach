"""
Document Service - Handles document upload, processing, and management
"""

import os
import sys
import uuid
import hashlib
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Any, Optional
import json

# Add ai_engine to path
sys.path.insert(0, str(Path(__file__).parent.parent.parent.parent / "ai_engine"))

from ..config import settings
from ..models.schemas import DocumentStatus, DocumentInfo, DocumentUploadResponse


class DocumentService:
    """Service for document management and processing"""
    
    def __init__(self):
        self.documents: Dict[str, DocumentInfo] = {}
        self._load_documents_state()
        
        # Lazy load AI engine components
        self._ingestion_pipeline = None
        self._embedding_service = None
        self._vector_store = None
    
    @property
    def ingestion_pipeline(self):
        """Lazy load ingestion pipeline"""
        if self._ingestion_pipeline is None:
            from ingestion import IngestionPipeline
            self._ingestion_pipeline = IngestionPipeline(
                chunk_size=settings.CHUNK_SIZE,
                chunk_overlap=settings.CHUNK_OVERLAP
            )
        return self._ingestion_pipeline
    
    @property
    def embedding_service(self):
        """Lazy load embedding service"""
        if self._embedding_service is None:
            from embeddings import EmbeddingService
            self._embedding_service = EmbeddingService(
                model_name=settings.EMBEDDING_MODEL
            )
        return self._embedding_service
    
    @property
    def vector_store(self):
        """Lazy load vector store"""
        if self._vector_store is None:
            from vectorstore import PineconeStore
            self._vector_store = PineconeStore()
        return self._vector_store
    
    def _load_documents_state(self):
        """Load documents state from disk"""
        state_file = settings.DATA_DIR / "documents_state.json"
        if state_file.exists():
            try:
                with open(state_file, "r") as f:
                    data = json.load(f)
                    for doc_id, doc_data in data.items():
                        doc_data["uploaded_at"] = datetime.fromisoformat(doc_data["uploaded_at"])
                        doc_data["status"] = DocumentStatus(doc_data["status"])
                        self.documents[doc_id] = DocumentInfo(**doc_data)
            except Exception as e:
                print(f"Error loading documents state: {e}")
    
    def _save_documents_state(self):
        """Save documents state to disk"""
        state_file = settings.DATA_DIR / "documents_state.json"
        try:
            data = {}
            for doc_id, doc_info in self.documents.items():
                data[doc_id] = {
                    "document_id": doc_info.document_id,
                    "filename": doc_info.filename,
                    "status": doc_info.status.value,
                    "chunk_count": doc_info.chunk_count,
                    "file_size_bytes": doc_info.file_size_bytes,
                    "uploaded_at": doc_info.uploaded_at.isoformat(),
                    "file_type": doc_info.file_type
                }
            with open(state_file, "w") as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving documents state: {e}")
    
    def _generate_document_id(self, filename: str, content: bytes) -> str:
        """Generate unique document ID"""
        hash_input = f"{filename}_{len(content)}_{datetime.now().isoformat()}"
        return hashlib.md5(hash_input.encode()).hexdigest()[:12]
    
    def _get_file_extension(self, filename: str) -> str:
        """Get file extension from filename"""
        return Path(filename).suffix.lower()
    
    def validate_file(self, filename: str, file_size: int) -> tuple[bool, str]:
        """Validate file before upload"""
        # Check extension
        ext = self._get_file_extension(filename)
        if ext not in settings.ALLOWED_EXTENSIONS:
            return False, f"File type {ext} not allowed. Allowed: {settings.ALLOWED_EXTENSIONS}"
        
        # Check size
        max_size = settings.MAX_FILE_SIZE_MB * 1024 * 1024
        if file_size > max_size:
            return False, f"File too large. Maximum: {settings.MAX_FILE_SIZE_MB}MB"
        
        return True, "OK"
    
    async def upload_document(
        self, 
        filename: str, 
        content: bytes
    ) -> DocumentUploadResponse:
        """Upload and process a document"""
        
        # Generate document ID
        document_id = self._generate_document_id(filename, content)
        file_type = self._get_file_extension(filename)
        
        # Create document info
        doc_info = DocumentInfo(
            document_id=document_id,
            filename=filename,
            status=DocumentStatus.PROCESSING,
            chunk_count=0,
            file_size_bytes=len(content),
            uploaded_at=datetime.now(),
            file_type=file_type
        )
        self.documents[document_id] = doc_info
        self._save_documents_state()
        
        try:
            # Save file temporarily
            temp_path = settings.UPLOAD_DIR / f"{document_id}_{filename}"
            with open(temp_path, "wb") as f:
                f.write(content)
            
            # Process document through ingestion pipeline
            processed = self.ingestion_pipeline.process_file(
                file_path=str(temp_path),
                document_id=document_id
            )
            
            # Generate embeddings
            texts = [chunk["content"] for chunk in processed.chunks]
            embeddings = self.embedding_service.embed_documents(texts)
            
            # Store in vector database
            ids = [f"{document_id}_{i}" for i in range(len(processed.chunks))]
            metadatas = [
                {
                    **chunk["metadata"],
                    "document_id": document_id,
                    "filename": filename
                }
                for chunk in processed.chunks
            ]
            
            self.vector_store.add_documents(
                ids=ids,
                embeddings=embeddings,
                contents=texts,
                metadatas=metadatas
            )

            
            # Update document status
            doc_info.status = DocumentStatus.READY
            doc_info.chunk_count = len(processed.chunks)
            self._save_documents_state()
            
            # Clean up temp file
            if temp_path.exists():
                temp_path.unlink()
            
            return DocumentUploadResponse(
                document_id=document_id,
                filename=filename,
                status=DocumentStatus.READY,
                message="Document processed successfully",
                chunk_count=len(processed.chunks),
                file_size_bytes=len(content)
            )
            
        except Exception as e:
            # Update status to error
            doc_info.status = DocumentStatus.ERROR
            self._save_documents_state()
            
            return DocumentUploadResponse(
                document_id=document_id,
                filename=filename,
                status=DocumentStatus.ERROR,
                message=f"Error processing document: {str(e)}",
                chunk_count=0,
                file_size_bytes=len(content)
            )
    
    def list_documents(self) -> List[DocumentInfo]:
        """List all documents"""
        return list(self.documents.values())
    
    def get_document(self, document_id: str) -> Optional[DocumentInfo]:
        """Get document by ID"""
        return self.documents.get(document_id)
    
    def delete_document(self, document_id: str) -> bool:
        """Delete document and its vectors"""
        if document_id not in self.documents:
            return False
        
        try:
            # Delete from vector store
            doc_info = self.documents[document_id]
            ids_to_delete = [
                f"{document_id}_{i}" 
                for i in range(doc_info.chunk_count)
            ]
            self.vector_store.delete(ids=ids_to_delete)
            
            # Remove from documents
            del self.documents[document_id]
            self._save_documents_state()
            
            return True
        except Exception as e:
            print(f"Error deleting document: {e}")
            return False


# Singleton instance
document_service = DocumentService()




