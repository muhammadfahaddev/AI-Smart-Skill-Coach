# Document Ingestion Pipeline
## AI Smart Skill Coach - v1.0

```mermaid
flowchart LR
    subgraph Upload["📤 UPLOAD"]
        A[("User Uploads<br/>Document")]
    end

    subgraph Validate["✅ VALIDATE"]
        B{"File Valid?<br/>Size, Type"}
    end

    subgraph Store["💾 STORE"]
        C[("Azure Blob<br/>Storage")]
    end

    subgraph Process["⚙️ PROCESS"]
        D["Extract Text<br/>(PyPDF2/pdfplumber)"]
        E["Chunk Text<br/>(500-1000 tokens)"]
    end

    subgraph Embed["🧠 EMBED"]
        F["Generate Embeddings<br/>(sentence-transformers)"]
    end

    subgraph VectorStore["📊 VECTOR STORE"]
        G[("ChromaDB<br/>Vector Database")]
    end

    subgraph DB["🗄️ DATABASE"]
        H[("MySQL<br/>Update Status")]
    end

    A --> B
    B -->|Valid| C
    B -->|Invalid| I[❌ Error Response]
    C --> D
    D --> E
    E --> F
    F --> G
    G --> H
    H --> J[✅ Ready for Q&A]

    style Upload fill:#e3f2fd
    style Validate fill:#fff3e0
    style Store fill:#e8f5e9
    style Process fill:#f3e5f5
    style Embed fill:#fce4ec
    style VectorStore fill:#e1f5fe
    style DB fill:#fffde7
```

## Pipeline Stages

| Stage | Technology | Input | Output |
|-------|------------|-------|--------|
| Upload | FastAPI | File (PDF/DOCX/TXT) | Blob URL |
| Validate | Pydantic | File metadata | Validation result |
| Store | Azure Blob | File bytes | Storage path |
| Extract | PyPDF2/pdfplumber | PDF file | Raw text |
| Chunk | LangChain | Raw text | Text chunks (500-1000 tokens) |
| Embed | sentence-transformers | Text chunks | Vectors (768 dims) |
| Store Vectors | ChromaDB | Embeddings | Vector IDs |
| Update DB | SQLAlchemy | Doc metadata | Status: "Ready" |

## Error Handling

| Error | Cause | Action |
|-------|-------|--------|
| Invalid Type | Unsupported format | Return 400 |
| Size Exceeded | > 10MB | Return 413 |
| Extraction Failed | Corrupted file | Retry OCR |
| Embedding Failed | Model error | Queue retry |
