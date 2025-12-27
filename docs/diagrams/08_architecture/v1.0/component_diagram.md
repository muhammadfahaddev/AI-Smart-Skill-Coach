# Component Diagram
## AI Smart Skill Coach - v2.0 (Multi-Tenant)

```mermaid
flowchart TB
    subgraph Presentation["PRESENTATION LAYER"]
        direction LR
        WA["Web App<br/>(Next.js)"]
        MA["Mobile App<br/>(Flutter)"]
        AP["Admin Panel<br/>(React)"]
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
        subgraph Services2["B2B Services"]
            direction LR
            ORG["Organization<br/>Service"]
            COHORT["Cohort<br/>Service"]
            ANALYTICS["Analytics<br/>Service"]
        end
        subgraph Services3["Support Services"]
            direction LR
            ASSESS["Assessment<br/>Service"]
            CERT["Certificate<br/>Service"]
            ADMIN["Admin<br/>Service"]
        end
    end

    subgraph AI["AI LAYER"]
        direction LR
        RAG["RAG Engine<br/>(LangChain)"]
        LLM["Fine-Tuned LLM<br/>(Gemini)"]
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

    WA & MA & AP -.-> AUTH
    DOC --> EMB
    CHAT --> RAG
    RAG --> LLM
    EMB --> VECTOR
    DOC --> BLOB
    AUTH --> MYSQL
    ORG --> MYSQL
    COHORT --> MYSQL
```

## Layer Description (Updated for B2B)

| Layer | Components | Technology |
|-------|------------|------------|
| Presentation | Web App, Mobile App, **Admin Panel** | Next.js, Flutter, React |
| Application | Auth, Document, Chat, Payment, **Org, Cohort**, Assessment, Cert, Analytics, Admin | Python FastAPI |
| AI | RAG Engine, LLM, Embeddings, Personalization | LangChain, Gemini |
| Data | MySQL, Vector DB, Blob Storage | Azure DB, ChromaDB, Azure Storage |

## New B2B Services

| Service | Responsibility | Dependencies |
|---------|----------------|--------------|
| **Organization Service** | Org CRUD, Seat Management, Billing | MySQL, Payment Service |
| **Cohort Service** | Class/Group Management, Enrollment | MySQL, Analytics |
| **Analytics Service** | Org-wide and Cohort-level reports | MySQL, All Services |

---

*Diagram Version: 2.0 | Updated for Multi-Tenant Architecture*
