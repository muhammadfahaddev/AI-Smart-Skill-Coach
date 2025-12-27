# Use Case Diagram
## AI Smart Skill Coach - v2.0 (Multi-Tenant)

```mermaid
flowchart LR
    subgraph System["«Subsystem»<br>AI Smart Skill Coach"]
        direction TB
        %% Core Use Cases
        UC1(("Register/<br>Login"))
        UC2(("Upload<br>Documents"))
        UC3(("Ask<br>Questions"))
        UC4(("View<br>Progress"))
        UC5(("Take<br>Assessment"))
        UC6(("Get<br>Certificate"))
        UC7(("Subscribe/<br>Pay"))
        
        %% B2B Use Cases
        UC12(("Create<br>Cohort"))
        UC13(("Invite<br>Students"))
        UC14(("View Cohort<br>Analytics"))
        UC15(("Manage<br>Org Seats"))
        UC16(("Org<br>Billing"))
        
        %% Admin Use Cases
        UC9(("Manage<br>Users"))
        UC10(("View<br>Analytics"))
        UC11(("System<br>Config"))
    end

    %% B2C Actors (Left)
    Student["🎓 Student"] --> UC1 & UC2 & UC3 & UC4 & UC5 & UC6
    Professional["💼 Professional"] --> UC1 & UC2 & UC3 & UC5 & UC6 & UC7
    
    %% B2B Actors (Left)
    Educator["👨‍🏫 Educator"] --> UC1 & UC2 & UC12 & UC13 & UC14
    OrgAdmin["🏢 Org Admin"] --> UC1 & UC15 & UC16 & UC14

    %% Admin Actors (Right)
    UC9 --> Admin["👔 Admin"]
    UC10 --> Admin
    UC11 --> SuperAdmin["🔐 Super Admin"]
    
    %% External Systems (Right)
    UC7 --> Stripe["Stripe<br>Payment"]
    UC3 --> AI["AI/LLM<br>Service"]
    UC2 --> VectorDB["Vector<br>Database"]

    %% Relationships
    UC3 -. «include» .-> UC2
    UC5 -. «include» .-> UC3
    UC6 -. «include» .-> UC5
    UC13 -. «include» .-> UC12
```

---

## Actor Classification (Updated for B2B)

| Side | Actor | Type | Description |
|------|-------|------|-------------|
| **Left** | 🎓 Student | Primary B2C | Individual learners, exam aspirants |
| **Left** | 💼 Professional | Primary B2C | Self-directed upskilling users |
| **Left** | 👨‍🏫 Educator | Primary B2B | Teachers, Coaches managing classes |
| **Left** | 🏢 Org Admin | Primary B2B | School/Company administrators |
| **Right** | 👔 Admin | Secondary | Platform moderators |
| **Right** | 🔐 Super Admin | Secondary | System administrators |
| **Right** | Stripe | Supporting | Payment gateway |
| **Right** | AI/LLM | Supporting | AI model service |
| **Right** | Vector DB | Supporting | Document storage |

---

## New B2B Use Cases

| Use Case | Actor | Description |
|----------|-------|-------------|
| Create Cohort | Educator | Create a class/group for students |
| Invite Students | Educator | Share enrollment key with students |
| View Cohort Analytics | Educator, Org Admin | See progress of all students in cohort |
| Manage Org Seats | Org Admin | Add/remove users within seat limit |
| Org Billing | Org Admin | Manage enterprise subscription |

---

## Use Case Relationships

### «include» Relationships
| Base Use Case | Included Use Case | Description |
|---------------|-------------------|-------------|
| Ask Questions | Upload Documents | Must upload docs before querying |
| Take Assessment | Ask Questions | Uses AI for quiz context |
| Get Certificate | Take Assessment | Must pass quiz first |
| Invite Students | Create Cohort | Must create cohort first |

---

*Diagram Version: 2.0 | Updated for Multi-Tenant B2B/B2C Architecture*
