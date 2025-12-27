# AI System Architecture
## AI Smart Skill Coach - v1.0

```mermaid
flowchart TB
    subgraph Presentation["📱 PRESENTATION LAYER"]
        WEB["🌐 Web App<br/>(Next.js)"]
        MOB["📱 Mobile App<br/>(Flutter)"]
    end

    subgraph API["🔌 API LAYER"]
        FASTAPI["FastAPI<br/>REST + WebSocket"]
    end

    subgraph AIEngine["🤖 AI ENGINE"]
        direction TB
        subgraph RAG["RAG Pipeline"]
            RETRIEVER["Retriever<br/>(Similarity Search)"]
            RERANKER["Re-ranker<br/>(Cross-Encoder)"]
        end
        subgraph LLM["Language Models"]
            FINETUNE["Fine-Tuned LLM<br/>(LoRA Adapters)"]
            FALLBACK["Fallback LLM<br/>(GPT-3.5)"]
        end
        LANGCHAIN["LangChain<br/>Orchestrator"]
    end

    subgraph Embedding["🧠 EMBEDDING"]
        EMBED_MODEL["Embedding Model<br/>(all-mpnet-base-v2)"]
    end

    subgraph Storage["💾 DATA LAYER"]
        MYSQL[("MySQL<br/>User Data")]
        VECTOR[("ChromaDB<br/>Vectors")]
        BLOB[("Azure Blob<br/>Documents")]
        REDIS[("Redis<br/>Cache")]
    end

    subgraph External["🌍 EXTERNAL"]
        STRIPE["💳 Stripe"]
        OPENAI["🤖 OpenAI API"]
        HUGGING["🤗 Hugging Face"]
    end

    WEB --> FASTAPI
    MOB --> FASTAPI
    
    FASTAPI --> LANGCHAIN
    LANGCHAIN --> RETRIEVER
    LANGCHAIN --> FINETUNE
    LANGCHAIN --> FALLBACK
    
    RETRIEVER --> VECTOR
    RETRIEVER --> RERANKER
    RERANKER --> LLM
    
    EMBED_MODEL --> VECTOR
    
    FASTAPI --> MYSQL
    FASTAPI --> BLOB
    FASTAPI --> REDIS
    
    FINETUNE --> HUGGING
    FALLBACK --> OPENAI
    FASTAPI --> STRIPE

    style Presentation fill:#e3f2fd
    style API fill:#fff3e0
    style AIEngine fill:#e8f5e9
    style Embedding fill:#f3e5f5
    style Storage fill:#fce4ec
    style External fill:#fffde7
```

## Layer Responsibilities

| Layer | Components | Technology | Purpose |
|-------|------------|------------|---------|
| Presentation | Web, Mobile | Next.js, Flutter | User interface |
| API | REST, WebSocket | FastAPI | Request handling |
| AI Engine | RAG, LLM | LangChain | Intelligence |
| Embedding | Model | sentence-transformers | Vector generation |
| Storage | DB, Vector, Blob | MySQL, ChromaDB, Azure | Data persistence |
| External | Payment, AI | Stripe, OpenAI | Third-party services |

## Data Flow

```
User Query → API → LangChain → Retriever → Vector Search
                                    ↓
              Response ← LLM ← Re-ranker ← Top-K Chunks
```

## Scaling Strategy

| Component | Scaling Method |
|-----------|----------------|
| API | Horizontal (K8s pods) |
| LLM | GPU instances + load balancer |
| Vector DB | Sharding by user_id |
| Cache | Redis cluster |
