# DFD Level 0 - Context Diagram
## AI Smart Skill Coach - v1.0

```mermaid
flowchart TB
    User["USER<br/>(Learner)"]
    Admin[" ADMIN"]
    Stripe["STRIPE<br/>Gateway"]
    
    System["AI SMART SKILL COACH<br/>SYSTEM"]
    
    User -->|"Documents, Questions"| System
    System -->|"Answers, Certificates"| User
    
    Admin -->|"Management Actions"| System
    System -->|"Reports, Analytics"| Admin
    
    System <-->|"Payment Processing"| Stripe
```

---

## External Entities

| Entity | Type | Data Flow In | Data Flow Out |
|--------|------|--------------|---------------|
| User | Primary Actor | Documents, Questions, Credentials | Answers, Certificates, Progress |
| Admin | Secondary Actor | Management Commands | Reports, Analytics |
| Stripe | External System | Payment Confirmation | Payment Requests |
