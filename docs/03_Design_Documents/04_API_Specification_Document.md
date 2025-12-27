# API Specification Document
## AI Smart Skill Coach

---

| Document Information | |
|---------------------|---------------------------|
| **Document ID** | API-SPEC-AISSC-001 |
| **Version** | 1.0 |
| **Date** | December 27, 2024 |
| **Status** | Draft |
| **Standard** | OpenAPI 3.0 |
| **Author** | Senior Backend Engineer |

---

# Table of Contents

1. [Introduction](#1-introduction)
2. [API Overview](#2-api-overview)
3. [Authentication](#3-authentication)
4. [Common Responses](#4-common-responses)
5. [API Endpoints](#5-api-endpoints)
6. [Data Models](#6-data-models)
7. [Rate Limiting](#7-rate-limiting)
8. [Versioning](#8-versioning)

---

# 1. Introduction

## 1.1 Purpose

Is document mein AI Smart Skill Coach ke complete REST API specifications defined hain, following OpenAPI 3.0 standard.

## 1.2 Base URLs

| Environment | Base URL |
|-------------|----------|
| Production | `https://api.aismartskillcoach.com/api/v1` |
| Staging | `https://staging-api.aismartskillcoach.com/api/v1` |
| Development | `http://localhost:8000/api/v1` |

## 1.3 API Standards

| Aspect | Standard |
|--------|----------|
| Protocol | HTTPS (TLS 1.3) |
| Format | JSON |
| Authentication | JWT Bearer Token |
| Error Format | RFC 7807 Problem Details |
| Date Format | ISO 8601 |

---

# 2. API Overview

## 2.1 API Services

| Service | Port | Base Path | Description |
|---------|------|-----------|-------------|
| Auth | 8001 | `/auth` | Authentication & Authorization |
| Documents | 8002 | `/documents` | Document Management |
| Chat | 8003 | `/chat` | AI Q&A |
| Quizzes | 8004 | `/quizzes` | Assessments |
| Payments | 8005 | `/payments` | Subscriptions & Billing |
| Users | 8001 | `/users` | User Profiles |

## 2.2 HTTP Methods

| Method | Usage |
|--------|-------|
| GET | Read resources |
| POST | Create resources |
| PUT | Full update |
| PATCH | Partial update |
| DELETE | Remove resources |

---

# 3. Authentication

## 3.1 JWT Token Structure

```json
{
  "header": {
    "alg": "HS256",
    "typ": "JWT"
  },
  "payload": {
    "sub": "user_uuid",
    "email": "user@example.com",
    "role": "PRO",
    "iat": 1703687400,
    "exp": 1703688300
  }
}
```

## 3.2 Token Configuration

| Token Type | Expiry | Usage |
|------------|--------|-------|
| Access Token | 15 minutes | API calls |
| Refresh Token | 7 days | Get new access token |

## 3.3 Authorization Header

```
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
```

---

# 4. Common Responses

## 4.1 Success Response

```json
{
  "success": true,
  "data": { ... },
  "message": "Operation successful"
}
```

## 4.2 Error Response (RFC 7807)

```json
{
  "type": "https://api.aismartskillcoach.com/errors/validation",
  "title": "Validation Error",
  "status": 400,
  "detail": "Email field is required",
  "instance": "/api/v1/auth/register"
}
```

## 4.3 HTTP Status Codes

| Code | Meaning | Usage |
|------|---------|-------|
| 200 | OK | Successful GET/PUT/PATCH |
| 201 | Created | Successful POST |
| 204 | No Content | Successful DELETE |
| 400 | Bad Request | Validation error |
| 401 | Unauthorized | Missing/invalid token |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource not exists |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Server Error | Internal error |

---

# 5. API Endpoints

---

## 5.1 Authentication API

### POST /auth/register

Register a new user.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "name": "John Doe"
}
```

**Response (201):**
```json
{
  "success": true,
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "user@example.com",
    "name": "John Doe",
    "role": "FREE"
  },
  "message": "Registration successful. Please verify your email."
}
```

---

### POST /auth/login

Authenticate user and get tokens.

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "SecurePass123!"
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "refresh_token": "dGhpcyBpcyBhIHJlZnJl...",
    "token_type": "Bearer",
    "expires_in": 900,
    "user": {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "email": "user@example.com",
      "name": "John Doe",
      "role": "PRO"
    }
  }
}
```

---

### POST /auth/refresh

Refresh access token.

**Request Body:**
```json
{
  "refresh_token": "dGhpcyBpcyBhIHJlZnJl..."
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "access_token": "eyJhbGciOiJIUzI1NiIs...",
    "expires_in": 900
  }
}
```

---

### POST /auth/logout

Invalidate refresh token.

**Headers:** `Authorization: Bearer <token>`

**Response (200):**
```json
{
  "success": true,
  "message": "Logged out successfully"
}
```

---

## 5.2 Documents API

### POST /documents/upload

Upload a new document.

**Headers:** 
- `Authorization: Bearer <token>`
- `Content-Type: multipart/form-data`

**Form Data:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| file | File | Yes | PDF/DOCX/TXT (max 50MB) |

**Response (201):**
```json
{
  "success": true,
  "data": {
    "id": "doc-550e8400-...",
    "filename": "machine_learning.pdf",
    "file_size": 2456789,
    "mime_type": "application/pdf",
    "status": "PROCESSING",
    "created_at": "2024-12-27T10:30:00Z"
  },
  "message": "Document uploaded. Processing started."
}
```

---

### GET /documents

List user's documents.

**Headers:** `Authorization: Bearer <token>`

**Query Parameters:**
| Param | Type | Default | Description |
|-------|------|---------|-------------|
| page | int | 1 | Page number |
| limit | int | 20 | Items per page |
| status | string | all | Filter by status |

**Response (200):**
```json
{
  "success": true,
  "data": {
    "documents": [
      {
        "id": "doc-550e8400-...",
        "filename": "machine_learning.pdf",
        "status": "READY",
        "chunk_count": 45,
        "created_at": "2024-12-27T10:30:00Z"
      }
    ],
    "pagination": {
      "page": 1,
      "limit": 20,
      "total": 5,
      "total_pages": 1
    }
  }
}
```

---

### GET /documents/{id}

Get document details.

**Response (200):**
```json
{
  "success": true,
  "data": {
    "id": "doc-550e8400-...",
    "filename": "machine_learning.pdf",
    "file_size": 2456789,
    "mime_type": "application/pdf",
    "status": "READY",
    "chunk_count": 45,
    "page_count": 120,
    "created_at": "2024-12-27T10:30:00Z"
  }
}
```

---

### DELETE /documents/{id}

Delete a document.

**Response (204):** No content

---

## 5.3 Chat API

### POST /chat/query

Ask a question (RAG Q&A).

**Headers:** `Authorization: Bearer <token>`

**Request Body:**
```json
{
  "question": "What is machine learning?",
  "document_ids": ["doc-550e8400-..."],
  "chat_history_id": "chat-abc123" 
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "answer": "Machine learning is a subset of artificial intelligence that enables systems to learn and improve from experience...",
    "sources": [
      {
        "document_id": "doc-550e8400-...",
        "filename": "machine_learning.pdf",
        "page_number": 12,
        "snippet": "...machine learning algorithms build a model based on sample data..."
      }
    ],
    "chat_history_id": "chat-abc123",
    "message_id": "msg-xyz789",
    "tokens_used": 450,
    "latency_ms": 2340
  }
}
```

---

### GET /chat/history

Get user's chat histories.

**Response (200):**
```json
{
  "success": true,
  "data": {
    "histories": [
      {
        "id": "chat-abc123",
        "title": "Machine Learning Basics",
        "message_count": 12,
        "created_at": "2024-12-27T10:30:00Z",
        "last_message_at": "2024-12-27T11:45:00Z"
      }
    ]
  }
}
```

---

### GET /chat/history/{id}

Get chat messages.

**Response (200):**
```json
{
  "success": true,
  "data": {
    "id": "chat-abc123",
    "title": "Machine Learning Basics",
    "messages": [
      {
        "id": "msg-001",
        "role": "user",
        "content": "What is machine learning?",
        "created_at": "2024-12-27T10:30:00Z"
      },
      {
        "id": "msg-002",
        "role": "assistant",
        "content": "Machine learning is...",
        "sources": [...],
        "created_at": "2024-12-27T10:30:02Z"
      }
    ]
  }
}
```

---

### POST /chat/feedback

Submit feedback on AI response.

**Request Body:**
```json
{
  "message_id": "msg-xyz789",
  "feedback": "positive" 
}
```

**Response (200):**
```json
{
  "success": true,
  "message": "Feedback recorded. Thank you!"
}
```

---

## 5.4 Quizzes API

### GET /quizzes

List available quizzes.

**Query Parameters:**
| Param | Type | Description |
|-------|------|-------------|
| domain | string | Filter by domain |
| difficulty | string | EASY/MEDIUM/HARD |

**Response (200):**
```json
{
  "success": true,
  "data": {
    "quizzes": [
      {
        "id": "quiz-001",
        "title": "Python Fundamentals",
        "domain": "IT",
        "difficulty": "MEDIUM",
        "question_count": 20,
        "time_limit_minutes": 30,
        "passing_score": 70,
        "is_premium": false
      }
    ]
  }
}
```

---

### POST /quizzes/{id}/start

Start a quiz attempt.

**Response (201):**
```json
{
  "success": true,
  "data": {
    "attempt_id": "attempt-abc123",
    "quiz_id": "quiz-001",
    "questions": [
      {
        "id": "q-001",
        "question_text": "What is a Python decorator?",
        "question_type": "MCQ",
        "options": [
          {"id": "A", "text": "A function modifier"},
          {"id": "B", "text": "A data type"},
          {"id": "C", "text": "A loop type"},
          {"id": "D", "text": "A class"}
        ]
      }
    ],
    "time_limit_minutes": 30,
    "started_at": "2024-12-27T10:30:00Z"
  }
}
```

---

### POST /quizzes/{id}/submit

Submit quiz answers.

**Request Body:**
```json
{
  "attempt_id": "attempt-abc123",
  "answers": [
    {"question_id": "q-001", "answer": "A"},
    {"question_id": "q-002", "answer": "B"}
  ]
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "attempt_id": "attempt-abc123",
    "score": 85.0,
    "correct_count": 17,
    "total_questions": 20,
    "passed": true,
    "time_taken_seconds": 1234,
    "certificate_id": "cert-xyz789"
  }
}
```

---

### GET /certificates/{id}

Get certificate details.

**Response (200):**
```json
{
  "success": true,
  "data": {
    "id": "cert-xyz789",
    "certificate_number": "CERT-2024-ABC123",
    "title": "Python Fundamentals Certification",
    "user_name": "John Doe",
    "score": 85.0,
    "issue_date": "2024-12-27",
    "verification_url": "https://verify.aismartskillcoach.com/CERT-2024-ABC123",
    "download_url": "https://api.aismartskillcoach.com/certificates/cert-xyz789/download"
  }
}
```

---

## 5.5 Payments API

### GET /plans

List subscription plans.

**Response (200):**
```json
{
  "success": true,
  "data": {
    "plans": [
      {
        "id": "plan-free",
        "name": "Free",
        "price": 0,
        "currency": "USD",
        "interval": "month",
        "features": ["5 documents", "50 queries/day", "Basic quizzes"]
      },
      {
        "id": "plan-pro",
        "name": "Pro",
        "price": 9.99,
        "currency": "USD",
        "interval": "month",
        "features": ["Unlimited documents", "500 queries/day", "All quizzes"]
      }
    ]
  }
}
```

---

### POST /subscriptions

Create a subscription.

**Request Body:**
```json
{
  "plan_id": "plan-pro",
  "payment_method_id": "pm_card_visa"
}
```

**Response (201):**
```json
{
  "success": true,
  "data": {
    "subscription_id": "sub-abc123",
    "status": "ACTIVE",
    "plan": "Pro",
    "current_period_start": "2024-12-27",
    "current_period_end": "2025-01-27"
  }
}
```

---

### POST /payments/checkout

Create Stripe checkout session.

**Request Body:**
```json
{
  "plan_id": "plan-pro",
  "success_url": "https://app.aismartskillcoach.com/success",
  "cancel_url": "https://app.aismartskillcoach.com/cancel"
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "checkout_url": "https://checkout.stripe.com/c/pay/cs_xxx"
  }
}
```

---

## 5.6 Organizations API (B2B)

### POST /organizations

Create a new organization.

**Headers:** `Authorization: Bearer <token>` (Requires PROFESSIONAL or higher role)

**Request Body:**
```json
{
  "name": "Acme Academy",
  "domain": "acme.edu"
}
```

**Response (201):**
```json
{
  "success": true,
  "data": {
    "id": "org-550e8400-...",
    "name": "Acme Academy",
    "domain": "acme.edu",
    "plan_type": "FREE",
    "seat_limit": 5,
    "owner_id": "user-abc..."
  }
}
```

---

### GET /organizations/{id}/members

List organization members.

**Response (200):**
```json
{
  "success": true,
  "data": {
    "members": [
      {
        "id": "user-123",
        "name": "Jane Educator",
        "email": "jane@acme.edu",
        "org_role": "ADMIN",
        "joined_at": "2024-12-27T10:30:00Z"
      }
    ],
    "total": 5,
    "seat_limit": 50
  }
}
```

---

### POST /organizations/{id}/invite

Invite users to organization.

**Request Body:**
```json
{
  "emails": ["student1@acme.edu", "student2@acme.edu"],
  "role": "MEMBER"
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "invites_sent": 2,
    "failed": []
  }
}
```

---

## 5.7 Cohorts/Classes API (Educators)

### POST /cohorts

Create a new cohort/class.

**Headers:** `Authorization: Bearer <token>` (Requires EDUCATOR role)

**Request Body:**
```json
{
  "name": "Physics 101 - Fall 2024",
  "org_id": "org-550e8400-...",
  "enrollment_key": "PHY101F24"
}
```

**Response (201):**
```json
{
  "success": true,
  "data": {
    "id": "cohort-abc...",
    "name": "Physics 101 - Fall 2024",
    "educator_id": "user-xyz...",
    "enrollment_key": "PHY101F24"
  }
}
```

---

### POST /cohorts/{id}/enroll

Students enroll using a key.

**Request Body:**
```json
{
  "enrollment_key": "PHY101F24"
}
```

**Response (200):**
```json
{
  "success": true,
  "message": "Enrolled in Physics 101 - Fall 2024"
}
```

---

### GET /cohorts/{id}/progress

Get cohort-level analytics (Educator only).

**Response (200):**
```json
{
  "success": true,
  "data": {
    "cohort_id": "cohort-abc...",
    "student_count": 25,
    "avg_score": 78.5,
    "at_risk_students": 3,
    "top_weak_areas": ["Thermodynamics", "Kinematics"]
  }
}
```

---

## 5.8 Users API

### GET /users/me

Get current user profile.

**Response (200):**
```json
{
  "success": true,
  "data": {
    "id": "550e8400-...",
    "email": "user@example.com",
    "name": "John Doe",
    "role": "PRO",
    "subscription": {
      "plan": "Pro",
      "status": "ACTIVE",
      "expires_at": "2025-01-27"
    },
    "stats": {
      "documents_count": 15,
      "quizzes_completed": 8,
      "certificates_earned": 3
    }
  }
}
```

---

### PATCH /users/me

Update user profile.

**Request Body:**
```json
{
  "name": "John Updated",
  "avatar_url": "https://..."
}
```

**Response (200):**
```json
{
  "success": true,
  "data": {
    "id": "550e8400-...",
    "name": "John Updated",
    "avatar_url": "https://..."
  }
}
```

---

# 6. Data Models

## 6.1 User Model (Updated for RBAC)

| Field | Type | Description |
|-------|------|-------------|
| id | uuid | Unique identifier |
| email | string | Email address |
| name | string | Display name |
| role | enum | **STUDENT/PROFESSIONAL/EDUCATOR/ORG_ADMIN/SUPER_ADMIN** |
| current_org_id | uuid | Active organization context (nullable) |
| is_verified | boolean | Email verified |
| created_at | datetime | Registration date |

## 6.2 Organization Model (New)

| Field | Type | Description |
|-------|------|-------------|
| id | uuid | Unique identifier |
| name | string | Organization name |
| domain | string | Email domain for auto-join |
| plan_type | enum | FREE/TEAM/ENTERPRISE |
| seat_limit | integer | Max users allowed |
| owner_id | uuid | Primary contact user |

## 6.3 Cohort Model (New)

| Field | Type | Description |
|-------|------|-------------|
| id | uuid | Unique identifier |
| name | string | Class/Cohort name |
| educator_id | uuid | Managing educator |
| org_id | uuid | Parent org (optional) |
| enrollment_key | string | Join code for students |

## 6.2 Document Model

| Field | Type | Description |
|-------|------|-------------|
| id | uuid | Unique identifier |
| filename | string | Original filename |
| status | enum | PENDING/PROCESSING/READY/FAILED |
| chunk_count | integer | Number of chunks |
| page_count | integer | Number of pages |

---

# 7. Rate Limiting

## 7.1 Limits by Tier

| Tier | Requests/min | Queries/day |
|------|--------------|-------------|
| Free | 30 | 50 |
| Pro | 100 | 500 |
| Premium | 300 | Unlimited |

## 7.2 Rate Limit Headers

| Header | Description |
|--------|-------------|
| X-RateLimit-Limit | Max requests allowed |
| X-RateLimit-Remaining | Requests remaining |
| X-RateLimit-Reset | Unix timestamp reset |

---

# 8. Versioning

## 8.1 URL Versioning

```
/api/v1/...  (current)
/api/v2/...  (future)
```

## 8.2 Deprecation Policy

| Phase | Duration | Action |
|-------|----------|--------|
| Announcement | 6 months | Deprecation notice |
| Sunset | 3 months | Warning headers |
| Removal | After sunset | 410 Gone response |

---

*Document Version: 1.0 | Standard: OpenAPI 3.0 | Last Updated: December 27, 2024*
