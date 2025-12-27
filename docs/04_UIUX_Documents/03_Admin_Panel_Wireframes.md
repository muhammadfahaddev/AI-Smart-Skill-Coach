# Admin Panel Wireframes
## AI Smart Skill Coach

---

| Document Information | |
|---------------------|---------------------------|
| **Document ID** | UIUX-WF-ADM-001 |
| **Version** | 3.0 |
| **Date** | December 28, 2024 |
| **Status** | Draft |
| **Platform** | Desktop Web (Admin) |
| **Author** | Senior UI/UX Designer |

---

# Table of Contents

1. [Dashboard & Analytics](#1-dashboard--analytics)
2. [User Management](#2-user-management)
3. [Content Management](#3-content-management)
4. [Financials](#4-financials)
5. [System Logs & Health](#5-system-logs--health)
6. [Access Control (RBAC)](#6-access-control-rbac)

---

# 1. Dashboard & Analytics

## 1.1 Executive Dashboard

```
┌──────────────────────────────────────────────────────────────────────┐
│  [Logo] Admin   [Search...]              [🔔] [Admin User ▼]         │
├────────┬─────────────────────────────────────────────────────────────┤
│ 📊 Dash│  OVERVIEW                                                   │
│ 👥 Usr │  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐            │
│ 📄 Doc │  │ Total Usr│ │ MRR     │ │ AI Calls│ │ Storage │            │
│ 💰 Fin │  │ 10,234  │ │ $45,230 │ │ 1.2M    │ │ 4.5 TB  │            │
│ ⚙️ Set │  │ +5%     │ │ +12%    │ │ +20%    │ │ 60% Full│            │
│        │  └─────────┘ └─────────┘ └─────────┘ └─────────┘            │
│        │                                                             │
│        │  ┌──────────────────────────┐  ┌─────────────────────────┐  │
│        │  │ User Growth (Line)       │  │ Geo Distribution (Map)  │  │
│        │  │        /                 │  │     US: 40%             │  │
│        │  │      _/                  │  │     EU: 30%             │  │
│        │  │   __/                    │  │     AS: 30%             │  │
│        │  └──────────────────────────┘  └─────────────────────────┘  │
│        │                                                             │
└────────┴─────────────────────────────────────────────────────────────┘
```

---

# 2. User Management

## 2.1 User List (Advanced Filter)

```
┌──────────────────────────────────────────────────────────────────────┐
│  👥 User Management                                     [ + Add User ]│
│                                                                      │
│  Filter:                                                             │
│  [ Role: All ▼ ] [ Status: All ▼ ] [ Date Joined: All Time ▼ ]       │
│                                                                      │
│  Search: [ Enter email or UUID...                        ] [ Go ]    │
│                                                                      │
│  NAME         EMAIL             ROLE      STATUS    SPENT     ACTION │
│  John Doe     john@a.com        PRO       Active    $120      [Edit] │
│  Jane Doe     jane@b.com        FREE      Banned    $0        [Edit] │
│  Admin One    admin@sys.com     ADMIN     Active    -         [Edit] │
│                                                                      │
│  [<] 1 2 3 4 5 ... 100 [>]                                           │
└──────────────────────────────────────────────────────────────────────┘
```

## 2.2 Edit User Modal

```
┌──────────────────────────────────────────────┐
│  Edit User: John Doe                         │
│                                              │
│  Usage Limits                                │
│  Docs Allowed: [ Unlimited ▼ ]               │
│  Daily Queries: [ 500       ]                │
│                                              │
│  Account Status                              │
│  (•) Active                                  │
│  ( ) Suspended (Reason needed)               │
│  ( ) Banned                                  │
│                                              │
│  Force Actions                               │
│  [ Reset Password ] [ Clear Sessions ]       │
│                                              │
│  [ Cancel ]                     [ Save ]     │
└──────────────────────────────────────────────┘
```

---

# 3. Content Management

## 3.1 Document Oversight

```
┌──────────────────────────────────────────────────────────────────────┐
│  📄 Global Document Repository                                       │
│                                                                      │
│  ID       NAME           OWNER       SIZE    TYPE    FLAGGED?  ACT   │
│  #9921    virus.exe.pdf  bad_user    5MB     PDF     YES (Saf) [Del] │
│  #9922    notes.docx     good_user   1MB     DOCX    NO        [View]│
│                                                                      │
│  Moderation Tools                                                    │
│  [ Bulk Delete Flagged Documents ]                                   │
└──────────────────────────────────────────────────────────────────────┘
```

---

# 4. Financials

## 4.1 Transaction Logs

```
┌──────────────────────────────────────────────────────────────────────┐
│  💰 Transaction History                                              │
│                                                                      │
│  DATE       ID         USER        AMOUNT   STATUS    GATEWAY        │
│  Dec 28     tx_123     john@a.com  $9.99    Succ      Stripe         │
│  Dec 28     tx_124     mike@b.com  $19.99   Fail      Stripe         │
│  Dec 27     tx_125     sue@c.com   $9.99    Refunded  Stripe         │
│                                                                      │
│  [ Export to CSV ]                                                   │
└──────────────────────────────────────────────────────────────────────┘
```

---

# 5. System Logs & Health

## 5.1 Audit Logs

```
┌──────────────────────────────────────────────────────────────────────┐
│  📜 System Audit Logs                                                │
│                                                                      │
│  TIME       ACTOR      ACTION            TARGET          IP          │
│  10:00:01   Admin1     User_Ban          user_123        192.168.1.1 │
│  10:05:22   System     DB_Backup         Weekly_22       Local       │
│  10:10:55   User22     Failed_Login      -               10.0.0.5    │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

## 5.2 Error Logs (Dev)

```
┌──────────────────────────────────────────────────────────────────────┐
│  ⚠️ Application Error Logs                                           │
│                                                                      │
│  LEVEL    MSG                            STACK TRACE       OCCURRENCES│
│  CRIT     DB Connection Timeout          at db.py:45       5          │
│  WARN     LLM Rate Limit Reached         at llm.py:102     120        │
│                                                                      │
│  [ Clear Logs ]  [ Download Dump ]                                   │
└──────────────────────────────────────────────────────────────────────┘
```

---

# 6. Access Control (RBAC)

## 6.1 Role Management

```
┌──────────────────────────────────────────────────────────────────────┐
│  🔐 Roles & Permissions                                              │
│                                                                      │
│  ROLE NAME      PERMISSIONS                                          │
│  Super Admin    [ALL]                                                │
│  Content Mod    [View Docs, Delete Docs, Ban Users]                  │
│  Support        [View Users, Reset Pass, View Logs]                  │
│                                                                      │
│  [ + Create Custom Role ]                                            │
└──────────────────────────────────────────────────────────────────────┘
```

---
*Document Version: 3.0 | 12 Screens | Administrative Controls*
