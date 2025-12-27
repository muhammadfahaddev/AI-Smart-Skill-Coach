# Enhanced UML Diagrams
## AI Smart Skill Coach - SRS Appendix

---

| Document Information | |
|---------------------|---------------------------|
| **Document ID** | SRS-UML-AISSC-002 |
| **Version** | 2.0 |
| **Date** | December 28, 2024 |
| **Author** | Senior Software Engineer |

---

## 1. Class Diagram

![Class Diagram](../diagrams/04_class/v1.0/Class%20Diagram-2025-12-27-161458.png)

---

## 2. Activity Diagram - Document Upload & Processing

![Document Upload Activity](../diagrams/06_activity/v1.0/document_upload.png)

---

## 3. Activity Diagram - Quiz & Certification Flow

![Quiz Certification Activity](../diagrams/06_activity/v1.0/quiz_certification.png)

---

## 4. Sequence Diagram - Authentication Flow

![Authentication Flow](../diagrams/03_sequence/v1.0/Authentication%20Flow-2025-12-27-160355.png)

---

## 5. New: Sequence Diagram - Cohort Enrollment (Educator Flow)

```mermaid
sequenceDiagram
    participant E as Educator
    participant API as Backend API
    participant DB as MySQL
    participant S as Student

    E->>API: POST /cohorts {name, enrollment_key}
    API->>DB: INSERT INTO cohorts
    DB-->>API: cohort_id
    API-->>E: Cohort Created, Share Key

    E->>S: Share Enrollment Key (Email/Manual)
    
    S->>API: POST /cohorts/enroll {key}
    API->>DB: SELECT cohort WHERE enrollment_key
    DB-->>API: cohort_id
    API->>DB: INSERT INTO cohort_enrollments
    API-->>S: Enrolled Successfully
```

---

## 6. New: Use Case Diagram - B2B Actors

```mermaid
graph LR
    subgraph Org Admin
        OA1[Manage Seats]
        OA2[View Org Analytics]
        OA3[Billing]
    end
    
    subgraph Educator
        E1[Create Cohort]
        E2[Assign Content]
        E3[View Student Progress]
    end
    
    subgraph Student
        S1[Enroll via Key]
        S2[Access Cohort Docs]
        S3[Take Quizzes]
    end
    
    OrgAdmin --> OA1
    OrgAdmin --> OA2
    OrgAdmin --> OA3
    
    Educator --> E1
    Educator --> E2
    Educator --> E3
    
    Student --> S1
    Student --> S2
    Student --> S3
```

---

*This document extends SRS Section 7 System Models & Diagrams - Version 2.0*
