# Sequence Diagram - Q&A Flow
## AI Smart Skill Coach - v1.0

```mermaid
sequenceDiagram
    autonumber
    participant U as User
    participant F as Frontend
    participant A as API Server
    participant R as RAG Engine
    participant V as Vector DB
    participant L as LLM

    U->>F: Ask question
    F->>A: POST /api/chat
    A->>A: Validate JWT
    A->>R: Process query
    R->>R: Generate query embedding
    R->>V: Similarity search
    V-->>R: Top-K relevant chunks
    R->>R: Build context prompt
    R->>L: Generate response
    L-->>R: AI answer
    R->>R: Extract source citations
    R-->>A: Answer + sources
    A->>A: Save to chat history
    A-->>F: JSON response
    F-->>U: Display answer with sources
```

---

## Flow Details

| Step | Component | Action |
|------|-----------|--------|
| 1-3 | Frontend → API | User submits question |
| 4-5 | RAG Engine | Convert question to embedding |
| 6-7 | Vector DB | Find similar document chunks |
| 8-10 | LLM | Generate answer from context |
| 11-14 | Response | Return answer with citations |
