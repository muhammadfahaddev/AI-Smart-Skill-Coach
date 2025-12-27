# Entity Relationship Overview
## AI Smart Skill Coach - v2.0 (Multi-Tenant)

```mermaid
erDiagram
    %% B2B Relationships
    ORGANIZATION ||--o{ ORGANIZATION_MEMBER : has
    ORGANIZATION ||--o{ COHORT : contains
    ORGANIZATION_MEMBER }o--|| USER : is
    COHORT ||--o{ COHORT_ENROLLMENT : has
    COHORT }o--|| USER : educator
    COHORT_ENROLLMENT }o--|| USER : student

    %% Core Relationships
    USER ||--o{ DOCUMENT : uploads
    USER ||--o{ CHAT_HISTORY : has
    USER ||--o{ USER_PROGRESS : tracks
    USER ||--o{ QUIZ_ATTEMPT : takes
    USER ||--|| SUBSCRIPTION : has

    DOCUMENT ||--o{ DOCUMENT_CHUNK : contains
    QUIZ ||--o{ QUESTION : has
    QUIZ_ATTEMPT ||--o| CERTIFICATE : generates
    SUBSCRIPTION ||--o{ PAYMENT : has

    %% New B2B Entities
    ORGANIZATION {
        uuid id PK
        string name
        string domain
        enum plan_type
        int seat_limit
        uuid owner_id FK
    }

    ORGANIZATION_MEMBER {
        uuid id PK
        uuid org_id FK
        uuid user_id FK
        enum org_role
        datetime joined_at
    }

    COHORT {
        uuid id PK
        uuid org_id FK
        uuid educator_id FK
        string name
        string enrollment_key
    }

    COHORT_ENROLLMENT {
        uuid id PK
        uuid cohort_id FK
        uuid user_id FK
        datetime enrolled_at
    }

    %% Core Entities
    USER {
        uuid id PK
        string email
        string password_hash
        string name
        enum role
        uuid current_org_id FK
        datetime created_at
    }

    DOCUMENT {
        uuid id PK
        uuid user_id FK
        uuid cohort_id FK
        string filename
        enum status
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
```

## Relationship Summary (Updated for B2B)

| Entity | Relationship | Related Entity | Description |
|--------|--------------|----------------|-------------|
| **ORGANIZATION** | 1:N | ORGANIZATION_MEMBER | Org has many members |
| **ORGANIZATION** | 1:N | COHORT | Org has many cohorts |
| **COHORT** | 1:N | COHORT_ENROLLMENT | Cohort has many enrolled students |
| USER | 1:N | DOCUMENT | User uploads documents |
| USER | 1:1 | SUBSCRIPTION | User has one subscription |
| QUIZ_ATTEMPT | 1:0..1 | CERTIFICATE | Generates cert if passed |

---

*Diagram Version: 2.0 | Updated for Multi-Tenant Architecture*
