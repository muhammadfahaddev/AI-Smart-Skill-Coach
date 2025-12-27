# System Context Diagram
## AI Smart Skill Coach - v2.0 (Multi-Tenant)

```mermaid
flowchart TB
    subgraph Users["👥 USERS"]
        subgraph B2C["B2C"]
            S["🎓 Students"]
            P["💼 Professionals"]
        end
        subgraph B2B["B2B"]
            E["👨‍🏫 Educators"]
            O["🏢 Org Admins"]
        end
        A["👔 Admin Users"]
    end

    subgraph Frontend["📱 FRONTEND"]
        WEB["🌐 Web Application<br/>(Next.js)"]
        MOB["📱 Mobile App<br/>(Flutter)"]
        ADMIN["🖥️ Admin Panel<br/>(React)"]
    end

    subgraph Backend["⚙️ BACKEND"]
        API["🔗 Backend API<br/>(FastAPI)"]
        ORG_SVC["🏢 Organization<br/>Service"]
        COHORT_SVC["👥 Cohort<br/>Service"]
    end

    subgraph AI["🤖 AI ENGINE"]
        RAG["RAG Engine<br/>(LangChain)"]
        LLM["Gemini LLM<br/>(Google AI)"]
        EMB["Embeddings<br/>(sentence-transformers)"]
    end

    subgraph Storage["💾 STORAGE"]
        DB[("MySQL<br/>Database")]
        VDB[("Vector DB<br/>ChromaDB")]
        BLOB[("Blob Storage<br/>Azure")]
    end

    subgraph External["🌍 EXTERNAL SERVICES"]
        STRIPE["💳 Stripe<br/>Payment Gateway"]
        EMAIL["📧 Email Service<br/>SendGrid"]
    end

    S & P <--> WEB
    S & P <--> MOB
    E & O <--> WEB
    A <--> ADMIN
    
    WEB --> API
    MOB --> API
    ADMIN --> API
    
    API --> ORG_SVC
    API --> COHORT_SVC
    API --> RAG
    RAG --> LLM
    RAG --> EMB
    EMB --> VDB
    
    API --> DB
    ORG_SVC --> DB
    COHORT_SVC --> DB
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

## Component Description (Updated for B2B)

| Component | Technology | Purpose |
|-----------|------------|---------|
| Web App | Next.js | User-facing web interface |
| Mobile App | Flutter | Cross-platform mobile app |
| **Admin Panel** | React | Org Admin & Super Admin console |
| Backend API | FastAPI | REST API & business logic |
| **Organization Svc** | FastAPI | Org CRUD, Seat Management |
| **Cohort Svc** | FastAPI | Class/Group Management |
| AI Engine | LangChain + Gemini | RAG & Q&A processing |
| MySQL | Azure Database | Relational data + Multi-tenant |
| Vector DB | ChromaDB | Embeddings (Namespaced per Org) |
| Stripe | Payment API | B2C Subscription + B2B Billing |

---

*Diagram Version: 2.0 | Updated for Multi-Tenant Architecture*
