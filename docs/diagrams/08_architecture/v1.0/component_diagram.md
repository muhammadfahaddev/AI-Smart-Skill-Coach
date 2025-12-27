# Component Diagram
## AI Smart Skill Coach - v1.0

```mermaid
flowchart TB
    subgraph Presentation["PRESENTATION LAYER"]
        direction LR
        WA["Web App<br/>(Next.js)"]
        MA["Mobile App<br/>(Flutter)"]
    end

    subgraph Application["APPLICATION LAYER"]
        direction TB
        subgraph Services1["Core Services"]
            direction LR
            AUTH["Auth<br/>Service"]
            DOC["Document<br/>Service"]
            CHAT["Chat<br/>Service"]
            PAY["Payment<br/>Service"]
        end
        subgraph Services2["Support Services"]
            direction LR
            ASSESS["Assessment<br/>Service"]
            CERT["Certificate<br/>Service"]
            ANALYTICS["Analytics<br/>Service"]
            ADMIN["Admin<br/>Service"]
        end
    end

    subgraph AI["AI LAYER"]
        direction LR
        RAG["RAG Engine<br/>(LangChain)"]
        LLM["Fine-Tuned LLM<br/>(LoRA/PEFT)"]
        EMB["Embedding Model<br/>(sentence-transformers)"]
        PERS["Personalization<br/>Engine"]
    end

    subgraph Data["DATA LAYER"]
        direction LR
        MYSQL[("MySQL<br/>(Azure DB)")]
        VECTOR[("Vector DB<br/>(ChromaDB)")]
        BLOB[("Blob Storage<br/>(Azure)")]
    end

    Presentation -->|REST API / WebSocket| Application
    Application --> AI
    AI --> Data

    WA & MA -.-> AUTH
    DOC --> EMB
    CHAT --> RAG
    RAG --> LLM
    EMB --> VECTOR
    DOC --> BLOB
    AUTH --> MYSQL
```

## Layer Description

| Layer | Components | Technology |
|-------|------------|------------|
| Presentation | Web App, Mobile App | Next.js, Flutter |
| Application | Auth, Document, Chat, Payment, Assessment, Cert, Analytics, Admin | Python FastAPI |
| AI | RAG Engine, LLM, Embeddings, Personalization | LangChain, LoRA/PEFT |
| Data | MySQL, Vector DB, Blob Storage | Azure DB, ChromaDB, Azure Storage |
