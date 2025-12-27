# Enhanced Data Model & ERD
## AI Smart Skill Coach - SRS Appendix

---

| Document Information | |
|---------------------|---------------------------|
| **Document ID** | SRS-ERD-AISSC-002 |
| **Version** | 2.0 |
| **Date** | December 28, 2024 |
| **Author** | Senior Database Engineer |

---

## 1. Entity Relationship Diagram (ERD)

![ERD Diagram](../diagrams/05_erd/v1.0/ER%20Diagram-2025-12-27-161616.png)

---

## 2. Multi-Tenant Data Architecture

### 2.1 Core Entities (Updated for RBAC)

| Entity | Description | Tenant Scope |
|--------|-------------|--------------|
| **users** | All platform users | Global |
| **organizations** | B2B entities (Schools, Companies) | Global |
| **organization_members** | User <-> Org mapping (M:M) | Per-Org |
| **cohorts** | Classes/Groups managed by Educators | Per-Org |
| **cohort_enrollments** | Student <-> Cohort mapping | Per-Cohort |
| **documents** | Uploaded learning materials | Per-User or Per-Cohort |
| **chat_histories** | AI conversation sessions | Per-User |

### 2.2 Tenant Isolation Strategy

| Isolation Level | Implementation | Use Case |
|-----------------|----------------|----------|
| **Column-Based** | `org_id` FK on all tenant tables | Standard B2B |
| **Row-Level Security** | DB Policies (Postgres) or App-Level Filtering (MySQL) | Shared DB |
| **Schema-Based** | Separate schema per org | Enterprise Clients |
| **Database-Based** | Separate DB per org | High-Security Orgs |

> ⚠️ **Senior DB Engineer Note:** For MySQL (our stack), we implement RLS at the application layer using SQLAlchemy query filters. All queries MUST include `WHERE org_id = current_org_id` for tenant-scoped tables.

---

## 3. Key Schema Changes for Multi-Tenancy

### 3.1 Users Table

```sql
ALTER TABLE users 
ADD COLUMN role ENUM('STUDENT', 'PROFESSIONAL', 'EDUCATOR', 'ORG_ADMIN', 'SUPER_ADMIN') DEFAULT 'STUDENT',
ADD COLUMN current_org_id CHAR(36) NULL,
ADD CONSTRAINT fk_users_current_org FOREIGN KEY (current_org_id) REFERENCES organizations(id);

CREATE INDEX idx_users_role ON users(role);
CREATE INDEX idx_users_org ON users(current_org_id);
```

### 3.2 New Tables

```sql
-- Organizations (B2B Tenants)
CREATE TABLE organizations (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    domain VARCHAR(100) UNIQUE COMMENT 'For email-based auto-join',
    plan_type ENUM('FREE', 'TEAM', 'ENTERPRISE') DEFAULT 'FREE',
    seat_limit INT UNSIGNED DEFAULT 5,
    owner_id CHAR(36) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    INDEX idx_org_domain (domain)
);

-- Org Membership (M:M with role)
CREATE TABLE organization_members (
    id CHAR(36) PRIMARY KEY,
    org_id CHAR(36) NOT NULL,
    user_id CHAR(36) NOT NULL,
    org_role ENUM('MEMBER', 'EDUCATOR', 'ADMIN', 'OWNER') DEFAULT 'MEMBER',
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY uk_org_user (org_id, user_id),
    FOREIGN KEY (org_id) REFERENCES organizations(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- Cohorts (Classes)
CREATE TABLE cohorts (
    id CHAR(36) PRIMARY KEY,
    org_id CHAR(36) NOT NULL,
    educator_id CHAR(36) NOT NULL,
    name VARCHAR(255) NOT NULL,
    enrollment_key VARCHAR(50) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (org_id) REFERENCES organizations(id) ON DELETE CASCADE,
    FOREIGN KEY (educator_id) REFERENCES users(id)
);
```

---

## 4. Database Security Features

| Feature | Implementation |
|---------|----------------|
| **Encryption at Rest** | AES-256 for sensitive columns |
| **Password Hashing** | bcrypt with cost 12 |
| **Soft Delete** | deleted_at column for GDPR |
| **Audit Trail** | audit_logs table for all changes |
| **Data Masking** | Email/phone masked in logs |
| **Tenant Isolation** | org_id filtering at query level |

---

## 5. Index Strategy (Optimized for Multi-Tenancy)

| Table | Index | Columns | Purpose |
|-------|-------|---------|---------|
| users | idx_email | email | Fast login lookup |
| users | idx_role | role | Role-based filtering |
| organization_members | idx_org_user | org_id, user_id | Membership check |
| documents | idx_user_docs | user_id, created_at | User document listing |
| documents | idx_cohort_docs | cohort_id, created_at | Cohort document sharing |
| cohorts | idx_org_cohorts | org_id | Org's cohort listing |
| audit_logs | idx_user_audit | user_id, created_at | Security auditing |

---

*This document extends SRS Section 8 Data Requirements - Version 2.0*
