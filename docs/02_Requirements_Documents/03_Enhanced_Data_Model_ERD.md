# Enhanced Data Model & ERD
## AI Smart Skill Coach - SRS Appendix

---

## 1. Entity Relationship Diagram (ERD)

![ERD Diagram](../diagrams/05_erd/v1.0/ER%20Diagram-2025-12-27-161616.png)

---

## 2. Database Security Features

| Feature | Implementation |
|---------|----------------|
| **Encryption at Rest** | AES-256 for sensitive columns |
| **Password Hashing** | bcrypt with cost 12 |
| **Soft Delete** | deleted_at column for GDPR |
| **Audit Trail** | audit_logs table for all changes |
| **Data Masking** | Email/phone masked in logs |
| **Row-Level Security** | User can only access own data |

---

## 3. Index Strategy

| Table | Index | Purpose |
|-------|-------|---------|
| users | email | Fast login lookup |
| documents | user_id, created_at | User document listing |
| chat_messages | session_id | Session history |
| quiz_attempts | user_id, quiz_id | Performance tracking |
| certificates | certificate_number | Verification lookup |
| audit_logs | user_id, created_at | Security auditing |

---

*This document extends SRS Section 8 Data Requirements*
