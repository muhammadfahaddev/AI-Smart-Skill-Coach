# RAG Pipeline Flowchart
## AI Smart Skill Coach - v1.0

```mermaid
flowchart TB
    subgraph Ingestion["📥 Document Ingestion"]
        A[📄 PDF Upload] --> B[📝 Text Extraction]
        B --> C[✂️ Text Chunking<br/>500-1000 tokens]
        C --> D[🔢 Generate Embeddings<br/>sentence-transformers]
        D --> E[(💾 Store in Vector DB<br/>ChromaDB/Weaviate)]
    end

    subgraph Query["❓ Query Processing"]
        F[💬 User Question] --> G[🔢 Embed Query]
        G --> H[🔍 Similarity Search<br/>Top-K retrieval]
        E --> H
        H --> I[📋 Build Context<br/>Prompt + Chunks]
        I --> J[🤖 LLM Generation<br/>Llama/Mistral]
        J --> K[📎 Add Source Citations]
        K --> L[✅ Return Answer]
    end

    A -.-> F

    style Ingestion fill:#e1f5fe
    style Query fill:#f3e5f5
```

---

## Pipeline Metrics

| Stage | Target |
|-------|--------|
| Text Extraction | 95%+ accuracy |
| Chunking | 500-1000 tokens |
| Embedding | 384/768 dimensions |
| Retrieval | Top 5-10 chunks |
| Response Time | < 5 seconds |
