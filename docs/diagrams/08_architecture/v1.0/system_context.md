# System Context Diagram
## AI Smart Skill Coach - Product Perspective

```mermaid
flowchart TB
    subgraph Users["👥 USERS"]
        L["👤 Learners<br/>(Free/Pro/Premium)"]
        A["👔 Admin Users"]
    end

    subgraph Frontend["📱 FRONTEND"]
        WEB["🌐 Web Application<br/>(Next.js)"]
        MOB["📱 Mobile App<br/>(Flutter)"]
    end

    subgraph Backend["⚙️ BACKEND"]
        API["🔗 Backend API<br/>(FastAPI)"]
    end

    subgraph AI["🤖 AI ENGINE"]
        RAG["RAG Engine<br/>(LangChain)"]
        LLM["Fine-Tuned LLM<br/>(LoRA/PEFT)"]
        EMB["Embeddings<br/>(sentence-transformers)"]
    end

    subgraph Storage["💾 STORAGE"]
        DB[("MySQL<br/>Database")]
        VDB[("Vector DB<br/>ChromaDB/Weaviate")]
        BLOB[("Blob Storage<br/>Azure")]
    end

    subgraph External["🌍 EXTERNAL SERVICES"]
        STRIPE["💳 Stripe<br/>Payment Gateway"]
        EMAIL["📧 Email Service<br/>SendGrid"]
    end

    L <--> WEB
    L <--> MOB
    A <--> WEB
    
    WEB --> API
    MOB --> API
    
    API --> RAG
    RAG --> LLM
    RAG --> EMB
    EMB --> VDB
    
    API --> DB
    API --> BLOB
    API --> STRIPE
    API --> EMAIL

    style Users fill:#e1f5fe
    style Frontend fill:#fff3e0
    style Backend fill:#e8f5e9
    style AI fill:#f3e5f5
    style Storage fill:#fce4ec
    style External fill:#fffde7
```

## Component Description

| Component | Technology | Purpose |
|-----------|------------|---------|
| Web App | Next.js | User-facing web interface |
| Mobile App | Flutter | Cross-platform mobile app |
| Backend API | FastAPI | REST API & business logic |
| AI Engine | LangChain + LLM | RAG & Q&A processing |
| MySQL | Azure Database | Relational data storage |
| Vector DB | ChromaDB | Embeddings storage & search |
| Stripe | Payment API | Subscription management |
