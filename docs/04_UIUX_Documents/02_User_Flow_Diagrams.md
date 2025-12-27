# User Flow Diagrams
## AI Smart Skill Coach

---

| Document Information | |
|---------------------|---------------------------|
| **Document ID** | UIUX-UF-AISSC-001 |
| **Version** | 1.0 |
| **Date** | December 28, 2024 |
| **Status** | Draft |
| **Author** | Senior UI/UX Designer |

---

# Table of Contents

1. [Overview](#1-overview)
2. [User Registration Flow](#2-user-registration-flow)
3. [Document Upload Flow](#3-document-upload-flow)
4. [AI Chat Flow](#4-ai-chat-flow)
5. [Quiz & Certification Flow](#5-quiz--certification-flow)
6. [Subscription Flow](#6-subscription-flow)

---

# 1. Overview

## 1.1 Purpose

Is document mein AI Smart Skill Coach ke major user flows documented hain jo user journeys ko visualize karte hain.

## 1.2 Flow Types

| Flow | Priority | Users |
|------|----------|-------|
| Registration | P0 | All |
| Document Upload | P0 | Learners |
| AI Chat | P0 | Learners |
| Quiz & Certification | P0 | Learners |
| Subscription | P1 | Learners |
| Admin Management | P2 | Admins |

---

# 2. User Registration Flow

## 2.1 Flow Diagram

```mermaid
flowchart TD
    A[🏠 Landing Page] --> B{Existing User?}
    B -->|Yes| C[🔐 Login Page]
    B -->|No| D[📝 Register Page]
    
    C --> E{Login Method}
    E -->|Email| F[Enter Email/Password]
    E -->|Google| G[Google OAuth]
    E -->|GitHub| H[GitHub OAuth]
    
    F --> I{Valid Credentials?}
    I -->|Yes| J[✅ Dashboard]
    I -->|No| K[❌ Error Message]
    K --> C
    
    G --> L{OAuth Success?}
    H --> L
    L -->|Yes| J
    L -->|No| M[❌ OAuth Error]
    M --> C
    
    D --> N[Enter Details]
    N --> O[Email/Password/Name]
    O --> P{Valid Input?}
    P -->|No| Q[❌ Validation Error]
    Q --> D
    P -->|Yes| R[Create Account]
    R --> S[📧 Send Verification Email]
    S --> T[⏳ Email Verification Pending]
    T --> U{Click Email Link}
    U --> V[✅ Account Verified]
    V --> J
```

## 2.2 Flow Steps

| Step | Action | Screen |
|------|--------|--------|
| 1 | User visits website | Landing Page |
| 2 | Clicks "Get Started" | Register Page |
| 3 | Enters email, password, name | Register Form |
| 4 | System validates input | - |
| 5 | Creates account | - |
| 6 | Sends verification email | - |
| 7 | User clicks email link | Email |
| 8 | Account verified | Dashboard |

---

# 3. Document Upload Flow

## 3.1 Flow Diagram

```mermaid
flowchart TD
    A[📊 Dashboard] --> B[📄 Documents Page]
    B --> C[📤 Click Upload]
    C --> D{Upload Method}
    
    D -->|Drag & Drop| E[Drop File]
    D -->|Click| F[File Browser]
    F --> G[Select File]
    
    E --> H{File Valid?}
    G --> H
    
    H -->|No - Size| I[❌ File too large]
    H -->|No - Type| J[❌ Invalid format]
    H -->|Yes| K[⏳ Uploading...]
    
    I --> C
    J --> C
    
    K --> L[☁️ Upload to Azure Blob]
    L --> M[📝 Create Document Record]
    M --> N[⏳ Processing Queue]
    N --> O[📖 Text Extraction]
    O --> P[✂️ Text Chunking]
    P --> Q[🔢 Generate Embeddings]
    Q --> R[💾 Store in ChromaDB]
    R --> S[✅ Document Ready]
    S --> T[🔔 Notify User]
    T --> U[📄 Document Available]
```

## 3.2 Flow Steps

| Step | Action | Status |
|------|--------|--------|
| 1 | User uploads file | PENDING |
| 2 | File stored in Azure | PROCESSING |
| 3 | Text extracted | PROCESSING |
| 4 | Text chunked | PROCESSING |
| 5 | Embeddings generated | PROCESSING |
| 6 | Stored in vector DB | READY |
| 7 | User notified | READY |

---

# 4. AI Chat Flow

## 4.1 Flow Diagram

```mermaid
flowchart TD
    A[📊 Dashboard] --> B[💬 Chat Page]
    B --> C{New or Existing?}
    
    C -->|New| D[➕ Create Chat]
    C -->|Existing| E[📜 Select Chat]
    
    D --> F[Select Document]
    E --> G[Load History]
    
    F --> H[💬 Chat Interface]
    G --> H
    
    H --> I[📝 User Types Question]
    I --> J[📤 Send Question]
    J --> K[🔢 Generate Query Embedding]
    K --> L[🔍 Vector Search]
    L --> M[📄 Retrieve Top-K Chunks]
    M --> N[📋 Assemble Context]
    N --> O[✨ Call LLM - Gemini]
    O --> P{Response Valid?}
    
    P -->|No| Q[⚠️ Fallback Response]
    P -->|Yes| R[📝 Generate Answer]
    
    Q --> S[💬 Display Response]
    R --> S
    
    S --> T[📑 Show Sources]
    T --> U{User Feedback?}
    
    U -->|👍| V[Record Positive]
    U -->|👎| W[Record Negative]
    U -->|None| H
    
    V --> H
    W --> H
```

## 4.2 RAG Query Steps

| Step | Component | Latency |
|------|-----------|---------|
| 1 | Query Embedding | < 50ms |
| 2 | Vector Search | < 200ms |
| 3 | Context Assembly | < 10ms |
| 4 | LLM Call | < 3s |
| 5 | Response Display | < 50ms |
| **Total** | | **< 5s** |

---

# 5. Quiz & Certification Flow

## 5.1 Flow Diagram

```mermaid
flowchart TD
    A[📊 Dashboard] --> B[📝 Quizzes Page]
    B --> C[📋 Browse Quizzes]
    C --> D{Quiz Type}
    
    D -->|Free| E[▶️ Start Quiz]
    D -->|Premium| F{User Tier?}
    
    F -->|Free| G[💳 Upgrade Prompt]
    F -->|Pro/Premium| E
    
    G --> H{Upgrade?}
    H -->|Yes| I[Subscription Flow]
    H -->|No| B
    I --> E
    
    E --> J[⏱️ Timer Starts]
    J --> K[📃 Display Question]
    
    K --> L{Answer?}
    L -->|Submit| M[Record Answer]
    L -->|Skip| N[Mark Skipped]
    
    M --> O{More Questions?}
    N --> O
    
    O -->|Yes| K
    O -->|No| P[📊 Calculate Score]
    
    P --> Q{Passed?}
    Q -->|No - Score < 70%| R[❌ Failed]
    Q -->|Yes - Score >= 70%| S[✅ Passed]
    
    R --> T[📈 Show Results]
    S --> U[🏆 Generate Certificate]
    U --> V[💾 Store Certificate]
    V --> W[📧 Email Certificate]
    W --> T
    
    T --> X{Retry?}
    X -->|Yes| E
    X -->|No| B
```

## 5.2 Certification Steps

| Step | Action | Output |
|------|--------|--------|
| 1 | Quiz completed | Score calculated |
| 2 | Passed (≥70%) | Certificate generated |
| 3 | PDF created | Stored in Azure |
| 4 | Email sent | User notified |
| 5 | Verification URL | Publicly verifiable |

---

# 6. Subscription Flow

## 6.1 Flow Diagram

```mermaid
flowchart TD
    A[📊 Dashboard] --> B[💳 Subscription Page]
    B --> C[📋 View Current Plan]
    C --> D{Want to Upgrade?}
    
    D -->|No| E[Stay on Current]
    D -->|Yes| F[🔄 Change Plan]
    
    F --> G[Compare Plans]
    G --> H{Select Plan}
    
    H -->|Pro| I[Pro - $9.99/mo]
    H -->|Premium| J[Premium - $19.99/mo]
    
    I --> K[💳 Checkout]
    J --> K
    
    K --> L[Stripe Checkout]
    L --> M{Payment Success?}
    
    M -->|No| N[❌ Payment Failed]
    N --> O[Retry or Cancel]
    O --> K
    
    M -->|Yes| P[✅ Payment Success]
    P --> Q[📧 Send Invoice]
    Q --> R[🔄 Update Subscription]
    R --> S[🔓 Unlock Features]
    S --> T[📊 Updated Dashboard]
    
    E --> T
```

## 6.2 Subscription Tiers

| Tier | Price | Documents | Queries/Day | Quizzes |
|------|-------|-----------|-------------|---------|
| Free | $0 | 5 | 50 | Basic |
| Pro | $9.99/mo | Unlimited | 500 | All |
| Premium | $19.99/mo | Unlimited | Unlimited | All + Priority |

---

# 7. User Flow Summary

## 7.1 Critical Paths

| Flow | Steps | Est. Time |
|------|-------|-----------|
| Registration | 8 steps | 2-3 min |
| Document Upload | 7 steps | 30 sec |
| AI Chat Query | 6 steps | < 5 sec |
| Complete Quiz | 5 steps | 20-30 min |
| Subscription | 6 steps | 2 min |

## 7.2 Error Handling

| Error | User Action | System Response |
|-------|-------------|-----------------|
| Invalid login | Re-enter credentials | Show error message |
| Upload failed | Retry upload | Show specific error |
| AI timeout | Retry query | Fallback response |
| Payment failed | Use different card | Show Stripe error |

---

*Document Version: 1.0 | Last Updated: December 28, 2024*
