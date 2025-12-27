# Entity Relationship Diagram (ERD)
## AI Smart Skill Coach - v1.0

```mermaid
erDiagram
    USERS ||--o{ DOCUMENTS : uploads
    USERS ||--o| SUBSCRIPTIONS : has
    USERS ||--o{ CHAT_SESSIONS : creates
    USERS ||--o{ QUIZ_ATTEMPTS : attempts
    USERS ||--o{ USER_PROGRESS : tracks
    USERS ||--o{ WEAK_AREAS : has
    USERS ||--o{ PAYMENTS : makes
    USERS ||--o{ AUDIT_LOGS : generates

    DOCUMENTS ||--o{ DOCUMENT_CHUNKS : contains

    CHAT_SESSIONS ||--o{ CHAT_MESSAGES : contains

    QUIZZES ||--o{ QUESTIONS : has
    QUIZZES ||--o{ QUIZ_ATTEMPTS : attempted

    QUIZ_ATTEMPTS ||--o| CERTIFICATES : generates

    USERS {
        uuid id PK
        string email UK
        string password_hash
        string name
        string avatar_url
        enum role
        boolean email_verified
        datetime created_at
        datetime updated_at
        datetime deleted_at
    }

    DOCUMENTS {
        uuid id PK
        uuid user_id FK
        string filename
        string original_name
        string file_path
        bigint file_size
        string mime_type
        enum status
        int chunk_count
        datetime created_at
    }

    DOCUMENT_CHUNKS {
        uuid id PK
        uuid document_id FK
        int chunk_index
        text content
        string embedding_id
        int page_number
        json metadata
        datetime created_at
    }

    CHAT_SESSIONS {
        uuid id PK
        uuid user_id FK
        string title
        datetime created_at
        datetime updated_at
    }

    CHAT_MESSAGES {
        uuid id PK
        uuid session_id FK
        enum role
        text content
        json sources
        enum feedback
        datetime created_at
    }

    QUIZZES {
        uuid id PK
        string title
        text description
        enum domain
        enum difficulty
        int passing_score
        int time_limit_mins
        boolean is_premium
        datetime created_at
    }

    QUESTIONS {
        uuid id PK
        uuid quiz_id FK
        text question_text
        enum question_type
        json options
        string correct_answer
        text explanation
        int order_index
    }

    QUIZ_ATTEMPTS {
        uuid id PK
        uuid user_id FK
        uuid quiz_id FK
        decimal score
        boolean passed
        json answers
        int time_taken_secs
        datetime started_at
        datetime completed_at
    }

    CERTIFICATES {
        uuid id PK
        uuid user_id FK
        uuid quiz_id FK
        uuid attempt_id FK
        string certificate_number UK
        date issue_date
        string pdf_path
        string verification_url
        datetime created_at
    }

    SUBSCRIPTIONS {
        uuid id PK
        uuid user_id FK
        enum plan_type
        enum status
        string stripe_customer_id
        string stripe_subscription_id
        datetime current_period_end
        datetime created_at
        datetime updated_at
    }

    PAYMENTS {
        uuid id PK
        uuid user_id FK
        string stripe_payment_id
        decimal amount
        string currency
        enum status
        string payment_method
        datetime created_at
    }

    USER_PROGRESS {
        uuid id PK
        uuid user_id FK
        string topic
        decimal completion_pct
        int time_spent_mins
        datetime last_studied
        int skill_level
    }

    WEAK_AREAS {
        uuid id PK
        uuid user_id FK
        string topic
        int weakness_score
        datetime detected_at
        boolean resolved
    }

    AUDIT_LOGS {
        uuid id PK
        uuid user_id FK
        string action
        string entity_type
        uuid entity_id
        string ip_address
        string user_agent
        json details
        datetime created_at
    }
```

---

## Key Constraints

| Table | Primary Key | Foreign Keys | Unique |
|-------|-------------|--------------|--------|
| users | id | - | email |
| documents | id | user_id | - |
| certificates | id | user_id, quiz_id, attempt_id | certificate_number |
| subscriptions | id | user_id | - |
