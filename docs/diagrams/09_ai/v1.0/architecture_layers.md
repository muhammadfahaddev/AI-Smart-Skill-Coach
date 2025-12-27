# Architecture Layers Diagram
## AI Smart Skill Coach - v1.0

```mermaid
flowchart TB
    subgraph Presentation["📱 PRESENTATION LAYER"]
        direction LR
        WEB["🌐 Web App<br/>(Next.js)"]
        MOB["📱 Mobile App<br/>(Flutter)"]
        ADMIN["👨‍💼 Admin Panel<br/>(Next.js)"]
    end

    subgraph Gateway["🔗 API GATEWAY"]
        NGINX["Nginx<br/>+ Rate Limiting"]
    end

    subgraph Application["⚙️ APPLICATION LAYER"]
        direction LR
        AUTH["🔐 Auth<br/>Service"]
        DOC["📄 Document<br/>Service"]
        CHAT["💬 Chat<br/>Service"]
        QUIZ["📝 Quiz<br/>Service"]
        PAY["💳 Payment<br/>Service"]
    end

    subgraph AI["🤖 AI ENGINE LAYER"]
        direction TB
        LANG["LangChain Orchestrator"]
        subgraph AIComponents[" "]
            direction LR
            RAG["🔍 RAG Engine<br/>+ Retriever"]
            LLM["🧠 Fine-Tuned<br/>LLM"]
            GUARD["🛡️ Guardrails<br/>& Safety"]
        end
    end

    subgraph Data["💾 DATA LAYER"]
        direction LR
        MYSQL[("MySQL<br/>(Users)")]
        CHROMA[("ChromaDB<br/>(Vectors)")]
        REDIS[("Redis<br/>(Cache)")]
        AZURE[("Azure Blob<br/>(Files)")]
    end

    WEB --> NGINX
    MOB --> NGINX
    ADMIN --> NGINX

    NGINX --> AUTH
    NGINX --> DOC
    NGINX --> CHAT
    NGINX --> QUIZ
    NGINX --> PAY

    AUTH --> MYSQL
    DOC --> CHROMA
    DOC --> AZURE
    CHAT --> LANG
    QUIZ --> MYSQL
    PAY --> MYSQL

    LANG --> RAG
    LANG --> LLM
    LANG --> GUARD
    RAG --> CHROMA

    style Presentation fill:#e3f2fd
    style Gateway fill:#fff3e0
    style Application fill:#e8f5e9
    style AI fill:#f3e5f5
    style Data fill:#fce4ec
```

## Layer Description

| Layer | Components | Technology |
|-------|------------|------------|
| Presentation | Web App, Mobile App, Admin Panel | Next.js, Flutter |
| API Gateway | Nginx, Rate Limiter | Nginx |
| Application | Auth, Document, Chat, Quiz, Payment | Python FastAPI |
| AI Engine | LangChain, RAG, Fine-Tuned LLM, Guardrails | LangChain, Gemini, Mistral |
| Data | MySQL, ChromaDB, Redis, Azure Blob | MySQL, ChromaDB, Redis |

## Component Communication

| From | To | Protocol |
|------|----|----------|
| Frontend | API Gateway | HTTPS |
| API Gateway | Services | HTTP/REST |
| Services | Databases | TCP |
| Chat Service | AI Engine | Async |
| AI Engine | LLM API | HTTPS |
