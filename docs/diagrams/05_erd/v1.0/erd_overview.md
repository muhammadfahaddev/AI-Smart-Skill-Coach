# Entity Relationship Overview
## AI Smart Skill Coach - v1.0

```mermaid
erDiagram
    USER ||--o{ DOCUMENT : uploads
    USER ||--o{ CHAT_HISTORY : has
    USER ||--o{ USER_PROGRESS : tracks
    USER ||--o{ WEAK_AREA : has
    USER ||--|| SUBSCRIPTION : has

    DOCUMENT ||--o{ DOCUMENT_CHUNK : contains

    QUIZ ||--o{ QUESTION : has
    USER ||--o{ QUIZ_ATTEMPT : takes
    QUIZ_ATTEMPT ||--o| CERTIFICATE : generates

    SUBSCRIPTION ||--o{ PAYMENT : has

    USER {
        uuid id PK
        string email
        string password_hash
        string name
        enum role
        datetime created_at
    }

    DOCUMENT {
        uuid id PK
        uuid user_id FK
        string filename
        string file_path
        enum status
    }

    CHAT_HISTORY {
        uuid id PK
        uuid user_id FK
        string title
        json messages
    }

    USER_PROGRESS {
        uuid id PK
        uuid user_id FK
        string topic
        int completion_pct
    }

    WEAK_AREA {
        uuid id PK
        uuid user_id FK
        string topic
        float weakness_score
    }

    QUIZ {
        uuid id PK
        string title
        enum domain
        int passing_score
    }

    QUIZ_ATTEMPT {
        uuid id PK
        uuid user_id FK
        uuid quiz_id FK
        decimal score
        boolean passed
    }

    CERTIFICATE {
        uuid id PK
        uuid attempt_id FK
        string certificate_number
        datetime issue_date
    }

    SUBSCRIPTION {
        uuid id PK
        uuid user_id FK
        enum plan_type
        enum status
    }

    PAYMENT {
        uuid id PK
        uuid subscription_id FK
        decimal amount
        enum status
    }
```

## Relationship Summary

| Entity | Relationship | Related Entity |
|--------|--------------|----------------|
| USER | 1:N | DOCUMENT, CHAT_HISTORY, USER_PROGRESS, WEAK_AREA, QUIZ_ATTEMPT |
| USER | 1:1 | SUBSCRIPTION |
| DOCUMENT | 1:N | DOCUMENT_CHUNK |
| QUIZ | 1:N | QUESTION |
| QUIZ_ATTEMPT | 1:0..1 | CERTIFICATE (if passed) |
| SUBSCRIPTION | 1:N | PAYMENT |
