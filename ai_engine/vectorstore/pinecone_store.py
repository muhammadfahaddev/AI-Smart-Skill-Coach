"""
Pinecone Vector Store
Cloud vector database for production
"""

from typing import List, Dict, Any, Optional
from .base_store import BaseVectorStore, SearchResult


class PineconeStore(BaseVectorStore):
    """Pinecone implementation for production."""
    
    def __init__(
        self,
        api_key: str = None,
        index_name: str = "ai-skill-coach",
        namespace: str = "default"
    ):
        """Initialize Pinecone store.
        
        Args:
            api_key: Pinecone API key
            index_name: Name of the index
            namespace: Namespace for multi-tenancy
        """
        self.index_name = index_name
        self.namespace = namespace
        self._index = None
        
        # Get API key from env if not provided
        if api_key is None:
            import os
from dotenv import load_dotenv
load_dotenv()
            api_key = os.getenv("PINECONE_API_KEY")
        
        self.api_key = api_key
    
    def _get_index(self):
        """Lazy load Pinecone index."""
        if self._index is None:
            from pinecone import Pinecone
            
            pc = Pinecone(api_key=self.api_key)
            self._index = pc.Index(self.index_name)
        
        return self._index
    
    def add_documents(
        self,
        ids: List[str],
        embeddings: List[List[float]],
        contents: List[str],
        metadatas: List[Dict[str, Any]] = None
    ) -> bool:
        """Add documents to Pinecone.
        
        Args:
            ids: Unique IDs for each document
            embeddings: Embedding vectors
            contents: Text content (stored in metadata)
            metadatas: Optional metadata
            
        Returns:
            Success status
        """
        index = self._get_index()
        
        try:
            vectors = []
            for i, (doc_id, emb, content) in enumerate(zip(ids, embeddings, contents)):
                metadata = metadatas[i] if metadatas else {}
                metadata["content"] = content  # Store content in metadata
                
                vectors.append({
                    "id": doc_id,
                    "values": emb,
                    "metadata": metadata
                })
            
            # Upsert in batches of 100
            batch_size = 100
            for i in range(0, len(vectors), batch_size):
                batch = vectors[i:i + batch_size]
                index.upsert(vectors=batch, namespace=self.namespace)
            
            return True
        except Exception as e:
            print(f"Error adding documents: {e}")
            return False
    
    def search(
        self,
        query_embedding: List[float],
        top_k: int = 5,
        filter: Dict[str, Any] = None
    ) -> List[SearchResult]:
        """Search for similar documents.
        
        Args:
            query_embedding: Query vector
            top_k: Number of results
            filter: Metadata filter
            
        Returns:
            List of search results
        """
        index = self._get_index()
        
        results = index.query(
            vector=query_embedding,
            top_k=top_k,
            namespace=self.namespace,
            filter=filter,
            include_metadata=True
        )
        
        search_results = []
        
        for match in results.get("matches", []):
            metadata = match.get("metadata", {})
            content = metadata.pop("content", "")
            
            search_results.append(SearchResult(
                id=match["id"],
                content=content,
                metadata=metadata,
                score=match["score"]
            ))
        
        return search_results
    
    def delete(self, ids: List[str]) -> bool:
        """Delete documents by ID.
        
        Args:
            ids: List of document IDs
            
        Returns:
            Success status
        """
        index = self._get_index()
        
        try:
            index.delete(ids=ids, namespace=self.namespace)
            return True
        except Exception as e:
            print(f"Error deleting documents: {e}")
            return False
    
    def count(self) -> int:
        """Get total document count."""
        index = self._get_index()
        stats = index.describe_index_stats()
        
        namespaces = stats.get("namespaces", {})
        if self.namespace in namespaces:
            return namespaces[self.namespace].get("vector_count", 0)
        return 0
    
    def delete_namespace(self):
        """Delete all vectors in namespace."""
        index = self._get_index()
        index.delete(delete_all=True, namespace=self.namespace)
