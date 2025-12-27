# Use Case Diagram
## AI Smart Skill Coach - v1.0

```mermaid
---
config:
  layout: fixed
---
flowchart LR
 subgraph System["«Subsystem»<br>AI Smart Skill Coach"]
    direction TB
        UC1(("Register/<br>Login"))
        UC2(("Upload<br>Documents"))
        UC3(("Ask<br>Questions"))
        UC4(("View<br>Progress"))
        UC5(("Take<br>Assessment"))
        UC6(("Get<br>Certificate"))
        UC7(("Subscribe/<br>Pay"))
        UC8(("Manage<br>Profile"))
        UC9(("Manage<br>Users"))
        UC10(("View<br>Analytics"))
        UC11(("Manage<br>Quizzes"))
  end
    UC3 -. «include» .-> UC2
    UC5 -. «include» .-> UC3
    UC6 -. «include» .-> UC5
    UC7 -. «include» .-> UC1
    UC4 -. «extend» .-> UC3
    UC8 -. «extend» .-> UC1
    User["User<br>(Learner)"] -- "1..*" --> UC1
    User --> UC2 & UC3 & UC4 & UC5 & UC6 & UC7 & UC8
    UC9 --> Admin["Admin"]
    UC10 --> Admin
    UC11 --> Admin
    UC8 --> Admin
    UC7 -- "0..*" --> Stripe["Stripe<br>Payment Service"]
    UC3 --> AI["AI/LLM<br>Service"]
    UC2 --> VectorDB["Vector<br>Database"]
```

---

## Actor Classification

| Side | Actor | Type | Description |
|------|-------|------|-------------|
| **Left** | User (Learner) | Primary | Main user of the system |
| **Right** | Admin | Secondary | Platform administrator |
| **Right** | Stripe Payment | Supporting | External payment gateway |
| **Right** | AI/LLM Service | Supporting | AI model provider |
| **Right** | Vector Database | Supporting | Document storage system |

---

## Use Case Relationships

### «include» Relationships
| Base Use Case | Included Use Case | Description |
|---------------|-------------------|-------------|
| Ask Questions | Upload Documents | Must upload docs before querying |
| Take Assessment | Ask Questions | Uses AI for quiz context |
| Get Certificate | Take Assessment | Must pass quiz first |
| Subscribe/Pay | Register/Login | Must be authenticated |

### «extend» Relationships
| Base Use Case | Extending Use Case | Condition |
|---------------|-------------------|-----------|
| Ask Questions | View Progress | When tracking learning |
| Register/Login | Manage Profile | When editing profile |

---

## Multiplicity

| Actor | Use Case | Multiplicity |
|-------|----------|--------------|
| User | Register/Login | 1..* (one user, many sessions) |
| User | Subscribe/Pay | 0..* (optional, multiple payments) |
| Stripe | Subscribe/Pay | 1 (single gateway) |
