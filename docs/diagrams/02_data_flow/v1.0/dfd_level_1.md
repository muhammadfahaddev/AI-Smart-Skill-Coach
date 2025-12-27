# DFD Level 1 - Detailed Data Flow
## AI Smart Skill Coach - v1.0

```mermaid
flowchart TB
    User["USER"]
    
    subgraph Processes
        P1["1.0<br/>User Management"]
        P2["2.0<br/>Document Processing"]
        P3["3.0<br/>RAG Q&A"]
        P4["4.0<br/>Learning Analytics"]
        P5["5.0<br/>Assessment & Certification"]
        P6["6.0<br/>Payment Processing"]
    end
    
    subgraph DataStores
        D1[("D1: User<br/>Database")]
        D2[("D2: Vector<br/>Database")]
        D3[("D3: Progress<br/>Database")]
        D4[("D4: Assessment<br/>Database")]
    end
    
    Stripe["STRIPE"]
    
    User -->|"Credentials"| P1
    P1 <-->|"User Data"| D1
    P1 -->|"Auth Token"| User
    
    User -->|"Documents"| P2
    P2 -->|"Chunks & Embeddings"| D2
    
    User -->|"Questions"| P3
    D2 -->|"Relevant Chunks"| P3
    P3 -->|"Answers"| User
    
    P3 -->|"Learning Data"| P4
    P4 <-->|"Progress"| D3
    P4 -->|"Recommendations"| User
    
    User -->|"Quiz Attempts"| P5
    P5 <-->|"Scores"| D4
    P5 -->|"Certificates"| User
    
    User -->|"Payment Request"| P6
    P6 <-->|"Payment Flow"| Stripe
```

---

## Process Descriptions

| Process | Description |
|---------|-------------|
| 1.0 User Management | Authentication, registration, profile |
| 2.0 Document Processing | Upload, extract, chunk, embed |
| 3.0 RAG Q&A | Retrieve context, generate answers |
| 4.0 Learning Analytics | Track progress, detect weak areas |
| 5.0 Assessment & Certification | Quizzes, scoring, certificates |
| 6.0 Payment Processing | Stripe integration, subscriptions |
