# Database Design Document (DDD)
## AI Smart Skill Coach

---

| Document Information | |
|---------------------|---------------------------|
| **Document ID** | DDD-AISSC-001 |
| **Version** | 1.0 |
| **Date** | December 27, 2024 |
| **Status** | Draft |
| **Author** | Senior Database Engineer |

---

# Table of Contents

1. [Introduction](#1-introduction)
2. [Database Architecture](#2-database-architecture)
3. [Conceptual Data Model](#3-conceptual-data-model)
4. [Logical Data Model](#4-logical-data-model)
5. [Physical Data Model](#5-physical-data-model)
6. [Table Specifications](#6-table-specifications)
7. [Indexes & Performance](#7-indexes--performance)
8. [Data Integrity](#8-data-integrity)
9. [Security Design](#9-security-design)
10. [Backup & Recovery](#10-backup--recovery)

---

# 1. Introduction

## 1.1 Purpose

Is document ka purpose AI Smart Skill Coach ke complete database design ko define karna hai, including schema, tables, relationships, indexes, aur data integrity constraints.

## 1.2 Scope

| In Scope | Out of Scope |
|----------|--------------|
| MySQL Schema Design | Vector Database (ChromaDB) |
| Table Specifications | File Storage (Azure Blob) |
| Indexes & Foreign Keys | Cache Design (Redis) |
| Security & Backup | Query Optimization Details |

## 1.3 Technology Stack

| Component | Technology |
|-----------|------------|
| **RDBMS** | MySQL 8.0 |
| **Cloud** | Azure Database for MySQL |
| **ORM** | SQLAlchemy |
| **Migrations** | Alembic |
| **Backup** | Azure Backup |

---

# 2. Database Architecture

## 2.1 Multi-Database Architecture

| Database | Type | Purpose |
|----------|------|---------|
| **MySQL** | Relational | User data, transactions, metadata |
| **ChromaDB** | Vector | Document embeddings, similarity search |
| **Redis** | Key-Value | Session cache, response cache |
| **Azure Blob** | Object | File storage (PDFs, certs) |

## 2.2 MySQL Configuration

```yaml
# Azure MySQL Configuration
server_version: 8.0
max_connections: 500
innodb_buffer_pool_size: 4G
character_set_server: utf8mb4
collation_server: utf8mb4_unicode_ci
```

---

# 3. Conceptual Data Model

## 3.1 Core Entities

| Entity | Description |
|--------|-------------|
| **User** | Platform users (learners, admins) |
| **Document** | Uploaded learning materials |
| **ChatHistory** | AI conversation records |
| **Quiz** | Assessment tests |
| **QuizAttempt** | User quiz attempts |
| **Certificate** | Issued certifications |
| **Subscription** | User subscription plans |
| **Payment** | Transaction records |

## 3.2 Entity Relationships

![ERD Overview](../diagrams/05_erd/v1.0/erd_overview.png)

---

# 4. Logical Data Model

## 4.1 Entity-Relationship Summary

| Entity | Relationships |
|--------|---------------|
| User | 1:N Documents, 1:N ChatHistory, 1:N QuizAttempts, 1:1 Subscription |
| Document | 1:N DocumentChunks |
| Quiz | 1:N Questions, 1:N QuizAttempts |
| QuizAttempt | N:1 User, N:1 Quiz, 0:1 Certificate |
| Subscription | N:1 User, 1:N Payments |

## 4.2 Cardinality Rules

| Relationship | Cardinality | Rule |
|--------------|-------------|------|
| User → Document | 1:N | User can upload many documents |
| User → Subscription | 1:1 | One active subscription per user |
| Quiz → Question | 1:N | Quiz has many questions |
| QuizAttempt → Certificate | 0:1 | Certificate only if passed |

---

# 5. Physical Data Model

## 5.1 Database Schema

```
Database: ai_smart_skill_coach
├── users
├── documents
├── document_chunks
├── chat_histories
├── chat_messages
├── quizzes
├── questions
├── quiz_attempts
├── quiz_answers
├── certificates
├── subscriptions
├── payments
├── user_progress
├── weak_areas
└── audit_logs
```

## 5.2 Schema Diagram

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   users     │─────│  documents  │─────│doc_chunks   │
└──────┬──────┘     └─────────────┘     └─────────────┘
       │
       ├──────────┬──────────┬──────────┐
       │          │          │          │
┌──────▼──────┐  ┌▼─────────┐┌▼────────┐┌▼───────────┐
│subscriptions│  │chat_hist ││quiz_att ││user_progr  │
└──────┬──────┘  └──────────┘└────┬────┘└────────────┘
       │                          │
┌──────▼──────┐              ┌────▼────┐
│  payments   │              │certific │
└─────────────┘              └─────────┘
```

---

# 6. Table Specifications

## 6.1 Users Table (Updated for RBAC)

```sql
CREATE TABLE users (
    id CHAR(36) PRIMARY KEY COMMENT 'UUID v4',
    email VARCHAR(255) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    name VARCHAR(100),
    role ENUM('STUDENT', 'PROFESSIONAL', 'EDUCATOR', 'ORG_ADMIN', 'SUPER_ADMIN') 
        DEFAULT 'STUDENT' COMMENT 'New Role definitions',
    current_org_id CHAR(36) COMMENT 'Active context for Multi-org users',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (current_org_id) REFERENCES organizations(id)
) ENGINE=InnoDB;
```

---

## 6.1.1 Organizations Table (New)

```sql
CREATE TABLE organizations (
    id CHAR(36) PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    domain VARCHAR(100) UNIQUE COMMENT 'Auto-join via email domain',
    plan_type ENUM('FREE', 'TEAM', 'ENTERPRISE') DEFAULT 'FREE',
    seat_limit INT UNSIGNED DEFAULT 5,
    owner_id CHAR(36) NOT NULL COMMENT 'Primary contact',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (owner_id) REFERENCES users(id)
) COMMENT='B2B Entities (Schools, Companies)';
```

---

## 6.1.2 Organization Members Table (New)

```sql
CREATE TABLE organization_members (
    id CHAR(36) PRIMARY KEY,
    org_id CHAR(36) NOT NULL,
    user_id CHAR(36) NOT NULL,
    org_role ENUM('MEMBER', 'ADMIN', 'OWNER') DEFAULT 'MEMBER',
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    UNIQUE KEY uk_org_user (org_id, user_id),
    FOREIGN KEY (org_id) REFERENCES organizations(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) COMMENT='Many-to-Many mapping for users in orgs';
```

---

## 6.1.3 Cohorts / Classes Table (New for Educators)

```sql
CREATE TABLE cohorts (
    id CHAR(36) PRIMARY KEY,
    org_id CHAR(36) COMMENT 'Optional linkage to Org',
    educator_id CHAR(36) NOT NULL,
    name VARCHAR(255) NOT NULL COMMENT 'e.g. Physics 101',
    description TEXT,
    enrollment_key VARCHAR(50) COMMENT 'Code for students to join',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (org_id) REFERENCES organizations(id) ON DELETE CASCADE,
    FOREIGN KEY (educator_id) REFERENCES users(id)
) COMMENT='Classes or Groups managed by Educators';
```

---

## 6.4 Chat Histories Table

```sql
CREATE TABLE chat_histories (
    id CHAR(36) PRIMARY KEY,
    user_id CHAR(36) NOT NULL,
    title VARCHAR(255) COMMENT 'Conversation title',
    document_id CHAR(36) COMMENT 'Related document (optional)',
    message_count INT UNSIGNED DEFAULT 0,
    is_archived BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (document_id) REFERENCES documents(id) ON DELETE SET NULL,
    INDEX idx_user_id (user_id),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
COMMENT='AI conversation sessions';
```

---

## 6.5 Chat Messages Table

```sql
CREATE TABLE chat_messages (
    id CHAR(36) PRIMARY KEY,
    chat_history_id CHAR(36) NOT NULL,
    role ENUM('user', 'assistant', 'system') NOT NULL,
    content TEXT NOT NULL,
    sources JSON COMMENT 'Source citations array',
    tokens_used INT UNSIGNED COMMENT 'Tokens consumed',
    latency_ms INT UNSIGNED COMMENT 'Response time in ms',
    feedback ENUM('positive', 'negative') COMMENT 'User feedback',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (chat_history_id) REFERENCES chat_histories(id) ON DELETE CASCADE,
    INDEX idx_chat_history_id (chat_history_id),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
COMMENT='Individual chat messages';
```

---

## 6.6 Quizzes Table

```sql
CREATE TABLE quizzes (
    id CHAR(36) PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    description TEXT,
    domain ENUM('IT', 'MEDICAL', 'BUSINESS', 'ACADEMIC', 'GENERAL') 
        DEFAULT 'GENERAL',
    difficulty ENUM('EASY', 'MEDIUM', 'HARD') DEFAULT 'MEDIUM',
    passing_score INT UNSIGNED DEFAULT 70 COMMENT 'Passing percentage',
    time_limit_minutes INT UNSIGNED DEFAULT 30,
    question_count INT UNSIGNED DEFAULT 0,
    is_active BOOLEAN DEFAULT TRUE,
    is_premium BOOLEAN DEFAULT FALSE COMMENT 'Premium-only quiz',
    price DECIMAL(10,2) DEFAULT 0.00 COMMENT 'Price if paid quiz',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    INDEX idx_domain (domain),
    INDEX idx_is_active (is_active)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
COMMENT='Assessment quizzes';
```

---

## 6.7 Questions Table

```sql
CREATE TABLE questions (
    id CHAR(36) PRIMARY KEY,
    quiz_id CHAR(36) NOT NULL,
    question_text TEXT NOT NULL,
    question_type ENUM('MCQ', 'TRUE_FALSE', 'SHORT_ANSWER') DEFAULT 'MCQ',
    options JSON COMMENT 'Array of options for MCQ',
    correct_answer VARCHAR(500) NOT NULL,
    explanation TEXT COMMENT 'Answer explanation',
    points INT UNSIGNED DEFAULT 1,
    order_index INT UNSIGNED NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (quiz_id) REFERENCES quizzes(id) ON DELETE CASCADE,
    INDEX idx_quiz_id (quiz_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
COMMENT='Quiz questions';
```

---

## 6.8 Quiz Attempts Table

```sql
CREATE TABLE quiz_attempts (
    id CHAR(36) PRIMARY KEY,
    user_id CHAR(36) NOT NULL,
    quiz_id CHAR(36) NOT NULL,
    score DECIMAL(5,2) COMMENT 'Score percentage',
    correct_count INT UNSIGNED DEFAULT 0,
    total_questions INT UNSIGNED,
    passed BOOLEAN DEFAULT FALSE,
    time_taken_seconds INT UNSIGNED,
    started_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    completed_at TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (quiz_id) REFERENCES quizzes(id) ON DELETE CASCADE,
    INDEX idx_user_id (user_id),
    INDEX idx_quiz_id (quiz_id),
    INDEX idx_passed (passed)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
COMMENT='User quiz attempts';
```

---

## 6.9 Certificates Table

```sql
CREATE TABLE certificates (
    id CHAR(36) PRIMARY KEY,
    quiz_attempt_id CHAR(36) NOT NULL UNIQUE,
    user_id CHAR(36) NOT NULL,
    certificate_number VARCHAR(50) NOT NULL UNIQUE COMMENT 'CERT-XXXXXX format',
    title VARCHAR(255) NOT NULL,
    file_path VARCHAR(500) COMMENT 'PDF path in Azure Blob',
    issue_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expiry_date TIMESTAMP COMMENT 'Optional expiry',
    is_valid BOOLEAN DEFAULT TRUE,
    verification_url VARCHAR(500) COMMENT 'Public verification URL',
    
    FOREIGN KEY (quiz_attempt_id) REFERENCES quiz_attempts(id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_certificate_number (certificate_number),
    INDEX idx_user_id (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
COMMENT='Issued certificates';
```

---

## 6.10 Subscriptions Table

```sql
CREATE TABLE subscriptions (
    id CHAR(36) PRIMARY KEY,
    user_id CHAR(36) NOT NULL UNIQUE COMMENT 'One subscription per user',
    plan_type ENUM('FREE', 'PRO', 'PREMIUM') DEFAULT 'FREE',
    stripe_subscription_id VARCHAR(255) COMMENT 'Stripe subscription ID',
    stripe_customer_id VARCHAR(255) COMMENT 'Stripe customer ID',
    status ENUM('ACTIVE', 'CANCELLED', 'EXPIRED', 'PAST_DUE') DEFAULT 'ACTIVE',
    current_period_start TIMESTAMP,
    current_period_end TIMESTAMP,
    cancel_at_period_end BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    INDEX idx_status (status),
    INDEX idx_stripe_subscription_id (stripe_subscription_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
COMMENT='User subscriptions';
```

---

## 6.11 Payments Table

```sql
CREATE TABLE payments (
    id CHAR(36) PRIMARY KEY,
    subscription_id CHAR(36) NOT NULL,
    stripe_payment_intent_id VARCHAR(255) UNIQUE,
    stripe_invoice_id VARCHAR(255),
    amount DECIMAL(10,2) NOT NULL,
    currency CHAR(3) DEFAULT 'USD',
    status ENUM('PENDING', 'SUCCEEDED', 'FAILED', 'REFUNDED') DEFAULT 'PENDING',
    payment_method VARCHAR(50) COMMENT 'card, bank_transfer, etc.',
    receipt_url VARCHAR(500),
    paid_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    
    FOREIGN KEY (subscription_id) REFERENCES subscriptions(id) ON DELETE CASCADE,
    INDEX idx_subscription_id (subscription_id),
    INDEX idx_status (status),
    INDEX idx_paid_at (paid_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
COMMENT='Payment transactions';
```

---

## 6.12 User Progress Table

```sql
CREATE TABLE user_progress (
    id CHAR(36) PRIMARY KEY,
    user_id CHAR(36) NOT NULL,
    topic VARCHAR(255) NOT NULL,
    completion_percentage DECIMAL(5,2) DEFAULT 0.00,
    documents_studied INT UNSIGNED DEFAULT 0,
    questions_answered INT UNSIGNED DEFAULT 0,
    correct_answers INT UNSIGNED DEFAULT 0,
    last_activity_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE KEY uk_user_topic (user_id, topic),
    INDEX idx_user_id (user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
COMMENT='User learning progress by topic';
```

---

## 6.13 Weak Areas Table

```sql
CREATE TABLE weak_areas (
    id CHAR(36) PRIMARY KEY,
    user_id CHAR(36) NOT NULL,
    topic VARCHAR(255) NOT NULL,
    weakness_score DECIMAL(3,2) DEFAULT 0.00 COMMENT '0-1 score',
    incorrect_count INT UNSIGNED DEFAULT 0,
    total_attempts INT UNSIGNED DEFAULT 0,
    last_detected_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_resolved BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    UNIQUE KEY uk_user_topic (user_id, topic),
    INDEX idx_user_weakness (user_id, weakness_score DESC)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
COMMENT='Detected weak areas for personalization';
```

---

# 7. Indexes & Performance

## 7.1 Index Summary

| Table | Index | Columns | Purpose |
|-------|-------|---------|---------|
| users | idx_email | email | Login lookup |
| documents | idx_user_id | user_id | User documents |
| chat_messages | idx_chat_history_id | chat_history_id | Message retrieval |
| quiz_attempts | idx_user_quiz | user_id, quiz_id | Attempt history |
| payments | idx_paid_at | paid_at | Revenue reports |

## 7.2 Query Optimization

| Query Pattern | Index Used |
|---------------|------------|
| User login by email | idx_email |
| User documents list | idx_user_id + idx_status |
| Chat history by user | idx_user_id + idx_created_at |
| Certificate verification | idx_certificate_number |

---

# 8. Data Integrity

## 8.1 Foreign Key Constraints

| Parent | Child | Action |
|--------|-------|--------|
| users | documents | ON DELETE CASCADE |
| users | subscriptions | ON DELETE CASCADE |
| documents | document_chunks | ON DELETE CASCADE |
| quizzes | questions | ON DELETE CASCADE |
| quiz_attempts | certificates | ON DELETE CASCADE |

## 8.2 Unique Constraints

| Table | Constraint | Columns |
|-------|------------|---------|
| users | email | email |
| subscriptions | user_id | user_id (1:1) |
| certificates | certificate_number | certificate_number |
| user_progress | uk_user_topic | user_id, topic |

---

# 9. Security Design

## 9.1 Data Encryption

| Data Type | Encryption |
|-----------|------------|
| Passwords | Bcrypt (cost 12) |
| At Rest | Azure TDE |
| In Transit | TLS 1.3 |
| PII Fields | AES-256 (optional) |

## 9.2 Access Control

| Role | Access Level |
|------|--------------|
| App Service | Read/Write (own data) |
| Admin Service | Full access |
| Analytics | Read-only |
| Backup | Read-only |

---

# 10. Backup & Recovery

## 10.1 Backup Strategy

| Type | Frequency | Retention |
|------|-----------|-----------|
| Full Backup | Daily | 30 days |
| Point-in-Time | Continuous | 7 days |
| Geo-Redundant | Real-time | Azure regional |

## 10.2 Recovery Objectives

| Metric | Target |
|--------|--------|
| RPO (Recovery Point) | < 5 minutes |
| RTO (Recovery Time) | < 1 hour |

---

*Document Version: 1.0 | Last Updated: December 27, 2024*
