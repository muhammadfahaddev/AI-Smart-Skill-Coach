# Web Application Wireframes
## AI Smart Skill Coach

---

| Document Information | |
|---------------------|---------------------------|
| **Document ID** | UIUX-WF-WEB-001 |
| **Version** | 3.0 |
| **Date** | December 28, 2024 |
| **Status** | Draft |
| **Platform** | Desktop Web (1920x1080) |
| **Author** | Senior UI/UX Designer |

---

# Table of Contents

1. [Layout Structure](#1-layout-structure)
2. [Public Pages](#2-public-pages)
3. [Authentication Flows](#3-authentication-flows)
4. [Learner Dashboard](#4-learner-dashboard)
5. [Document Management](#5-document-management)
6. [AI Learning Interface](#6-ai-learning-interface)
7. [Assessments & Certification](#7-assessments--certification)
8. [User Profile & Settings](#8-user-profile--settings)
9. [Subscription & Billing](#9-subscription--billing)
10. [Error & Empty States](#10-error--empty-states)

---

# 1. Layout Structure

## 1.1 Global Navigation (LoggedIn)

```
┌──────────────────────────────────────────────────────────────────────┐
│  [Logo] AISSC   [Search 🔍             ]   [🔔 2] [? Help] [User ▼]  │
├───────┬──────────────────────────────────────────────────────────────┤
│ 🏠    │                                                              │
│ Home  │  [ Breadcrumb > Path ]                                       │
│ 📄    │                                                              │
│ Docs  │  +--------------------------------------------------------+  │
│ 💬    │  |                                                        |  │
│ Chat  │  |                 PAGE CONTENT                           |  │
│ 📝    │  |                                                        |  │
│ Quiz  │  +--------------------------------------------------------+  │
│ ⚙️    │                                                              │
│ Setgs │  [ Footer: Privacy • Terms • v1.0 ]                          │
└───────┴──────────────────────────────────────────────────────────────┘
```

---

# 2. Public Pages

## 2.1 Landing Page Hero

```
┌──────────────────────────────────────────────────────────────────────┐
│  [Logo]         Product   Features   Pricing   Blog         [ Login ]│
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│          Learn Faster with AI                                        │
│          [ Upload PDF ] [ Ask Question ] [ Get Answer ]              │
│                                                                      │
│          Join 10,000+ Students                                       │
│          [ Email Address         ] [ Get Started Free ]              │
│                                                                      │
│    [ Hero Image: Dashboard Mockup floating ]                         │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

## 2.2 Pricing Page

```
┌──────────────────────────────────────────────────────────────────────┐
│  Simple, Transparent Pricing                                         │
│                                                                      │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                │
│  │    FREE      │  │    PRO       │  │    TEAM      │                │
│  │     $0       │  │   $9.99      │  │   Custom     │                │
│  ├──────────────┤  ├──────────────┤  ├──────────────┤                │
│  │ 5 Docs       │  │ Unlimited    │  │ Unlim + API  │                │
│  │ 50 Queries   │  │ 500 Queries  │  │ Prior. Supp  │                │
│  │ Community    │  │ Email Supp   │  │ Dedicated    │                │
│  │ [ Join ]     │  │ [ Buy Now ]  │  │ [ Contact ]  │                │
│  └──────────────┘  └──────────────┘  └──────────────┘                │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

## 2.3 Contact Us

```
┌──────────────────────────────────────────────────────────────────────┐
│  Get in Touch                                                        │
│                                                                      │
│  ┌───────────────────────────┐  📍 Address: 123 AI Street           │
│  │ Name                      │  📧 Email: support@aissc.com         │
│  ├───────────────────────────┤                                      │
│  │ Email                     │  Frequently Asked Questions          │
│  ├───────────────────────────┤  > How do I update my card?          │
│  │ Subject                   │  > Is my data private?               │
│  ├───────────────────────────┤                                      │
│  │ Message...                │                                      │
│  │                           │                                      │
│  │ [ Send Message ]          │                                      │
│  └───────────────────────────┘                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

# 3. Authentication Flows

## 3.1 Login

```
┌──────────────────────────────────────────────────────────────────────┐
│  [Logo]                                                              │
│                                                 Don't have account?  │
│  Sign In to AI Coach                            [ Create Account ]   │
│                                                                      │
│  [ Email Address     ]                                               │
│  [ Password          ]  [ Forgot? ]                                  │
│                                                                      │
│  [ Sign In ]                                                         │
│                                                                      │
│  -- OR --                                                            │
│  [ G  Google ]  [ Gh GitHub ]                                        │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

## 3.2 Register

```
┌──────────────────────────────────────────────────────────────────────┐
│  Create your account                                                 │
│                                                                      │
│  [ Full Name         ]                                               │
│  [ Email Address     ]                                               │
│  [ Password          ] (Must be 8+ chars)                            │
│  [ Confirm Password  ]                                               │
│                                                                      │
│  [x] I agree to Terms & Privacy                                      │
│                                                                      │
│  [ Create Account ]                                                  │
└──────────────────────────────────────────────────────────────────────┘
```

## 3.3 Forgot Password

```
┌──────────────────────────────────────────────────────────────────────┐
│  Reset Password                                                      │
│                                                                      │
│  Enter your email to receive a reset link.                           │
│                                                                      │
│  [ user@example.com    ]                                             │
│                                                                      │
│  [ Send Reset Link ]                                                 │
│                                                                      │
│  < Back to Login                                                     │
└──────────────────────────────────────────────────────────────────────┘
```

## 3.4 Email Verification

```
┌──────────────────────────────────────────────────────────────────────┐
│  ✉️ Check your email                                                │
│                                                                      │
│  We sent a 6-digit code to user@example.com                          │
│                                                                      │
│  [  1  ] [  2  ] [  3  ] [  4  ] [  5  ] [  6  ]                     │
│                                                                      │
│  [ Verify Email ]                                                    │
│                                                                      │
│  Didn't receive it? [ Resend ]                                       │
└──────────────────────────────────────────────────────────────────────┘
```

---

# 4. Learner Dashboard

## 4.1 Main View

```
┌──────────────────────────────────────────────────────────────────────┐
│  👋 Good Afternoon, John!                                            │
│                                                                      │
│  ┌── Quick Stats ──────────────────────────────────────────────────┐ │
│  │ 📄 15 Docs    💬 450 Queries    🏆 3 Certs    🔥 7 Day Streak   │ │
│  └─────────────────────────────────────────────────────────────────┘ │
│                                                                      │
│  ┌── Continue Learning ────────────────────────────────────────────┐ │
│  │  ┌────────────┐  ┌────────────┐  ┌────────────┐                 │ │
│  │  │ ML Basics  │  │ Python 101 │  │ SQL Adv    │                 │ │
│  │  │ [ Resume ] │  │ [ Resume ] │  │ [ Resume ] │                 │ │
│  │  └────────────┘  └────────────┘  └────────────┘                 │ │
│  └─────────────────────────────────────────────────────────────────┘ │
│                                                                      │
│  ┌── Recent Activity ─────────────────┐  ┌── Recommended ──────────┐ │
│  │ • You scored 80% in Py Quiz (2h)   │  │ 📝 Advanced Python Quiz │ │
│  │ • Uploaded React_Notes.pdf (5h)    │  │ 📄 Intro to Neural Nets │ │
│  │ • Asked 15 questions about ML      │  │                         │ │
│  │ [ View History ]                   │  │ [ Explore ]             │ │
│  └────────────────────────────────────┘  └─────────────────────────┘ │
└──────────────────────────────────────────────────────────────────────┘
```

## 4.2 Empty State (New User)

```
┌──────────────────────────────────────────────────────────────────────┐
│  👋 Welcome to AI Smart Skill Coach!                                 │
│                                                                      │
│          [ Illustration: Empty Box ]                                 │
│                                                                      │
│      It looks a bit empty here. Let's get you started!               │
│                                                                      │
│     ┌──────────────────────────────────────────────────┐             │
│     │ 1️⃣  Upload your first PDF document               │             │
│     │     [ Upload Now ]                               │             │
│     │                                                  │             │
│     │ 2️⃣  Ask AI to summarize it                       │             │
│     │     (Waiting for doc...)                         │             │
│     └──────────────────────────────────────────────────┘             │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

# 5. Document Management

## 5.1 Document List

```
┌──────────────────────────────────────────────────────────────────────┐
│  My Documents                               [ + Upload New ]         │
│                                                                      │
│  [ Search...           ]  Filter: [ All  ▼ ]  Sort: [ Date ▼ ]       │
│                                                                      │
│  NAME                  STATUS      SIZE      DATE         ACTIONS    │
│  ──────────────────────────────────────────────────────────────────  │
│  📄 Intro_to_AI.pdf    ✅ Ready    2.4 MB    Dec 28      [💬] [⋮]    │
│  📄 Data_Science.docx  ✅ Ready    1.1 MB    Dec 27      [💬] [⋮]    │
│  📄 Bad_File.txt       ❌ Error    0.1 MB    Dec 26      [RETRY]     │
│  📄 History.pdf        ⏳ 45%      5.0 MB    Dec 28      [CANCEL]    │
│                                                                      │
│  Showing 1-4 of 4                                     <  1  >        │
└──────────────────────────────────────────────────────────────────────┘
```

## 5.2 Document Context Menu

```
┌──────────────────────┐
│ [💬 Chat with Doc  ] │
│ [✏️ Rename         ] │
│ [⬇️ Download       ] │
│ [🗂️ Move to Folder ] │
│ -------------------- │
│ [🗑️ Delete         ] │
└──────────────────────┘
```

## 5.3 Document Details

```
┌──────────────────────────────────────────────────────────────────────┐
│  < Back   📄 Intro_to_AI.pdf                                         │
│                                                                      │
│  ┌───────────────────────┐  ┌─────────────────────────────────────┐  │
│  │ [ Thumbnail Preview ] │  │ Metadata                            │  │
│  │                       │  │ Status: ✅ Processed                │  │
│  │                       │  │ Chunks: 45                          │  │
│  │                       │  │ Characters: 25,000                  │  │
│  │ [ View Original ]     │  │ Uploaded: Dec 28, 2024              │  │
│  └───────────────────────┘  │ Type: application/pdf               │  │
│                             └─────────────────────────────────────┘  │
│  Summary                                                             │
│  This document covers the basics of Artificial Intelligence (AI),    │
│  including its history, types (Narrow vs General), and applications. │
│                                                                      │
│  Key Entities                                                        │
│  [Supervised Learning] [Neural Networks] [Turing Test]               │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

## 5.4 Delete Confirmation Modal

```
┌──────────────────────────────────────────────┐
│  🗑️ Delete Document?                         │
│                                              │
│  Are you sure you want to delete             │
│  "Intro_to_AI.pdf"?                          │
│                                              │
│  This action cannot be undone. All chat      │
│  history associated with this doc will       │
│  also be deleted.                            │
│                                              │
│  [ Cancel ]              [ Delete Permanently]│
└──────────────────────────────────────────────┘
```

---

# 6. AI Learning Interface

## 6.1 Split Request View

```
┌───────────────────────────┬──────────────────────────────────────────┐
│ 📄 PDF Viewer             │ 💬 AI Assistant                          │
│ [ Zoom ] [ Page 1/12 ]    │                                          │
│                           │ [ User ]                                 │
│ LOREM IPSUM               │ Summarize this page.                     │
│                           │                                          │
│ Text contents of the      │ [ AI Coach ]                             │
│ document appear here...   │ This page discusses...                   │
│ Highlighted text          │                                          │
│ shows references.         │ [ User ]                                 │
│                           │ What does "Lorem" mean?                  │
│                           │                                          │
│                           │ [ AI Coach ]                             │
│                           │ Lorem Ipsum is dummy text...             │
│                           │                                          │
│                           │ 📄 Ref: Page 1, Para 2 [ Jump ]          │
│                           │ [👍 Helpful] [👎 Bad] [📋 Copy]          │
│                           │                                          │
│                           ├──────────────────────────────────────────┤
│                           │ [ Paperclip ] [ Type message...     ] ➤  │
└───────────────────────────┴──────────────────────────────────────────┘
```

## 6.2 Chat with Multiple Docs (Selection)

```
┌──────────────────────────────────────────────────────────────────────┐
│  Select Documents for Chat                                   [ X ]   │
│                                                                      │
│  [ Search... ]                                                       │
│                                                                      │
│  [ ] Select All                                                      │
│  [x] 📄 Intro_to_AI.pdf                                              │
│  [x] 📄 Advanced_AI.pdf                                              │
│  [ ] 📄 Biology_101.pdf                                              │
│                                                                      │
│  2 Selected                                      [ Start Chat ]      │
└──────────────────────────────────────────────────────────────────────┘
```

---

# 7. Assessments & Certification

## 7.1 Quiz Overview & Selection

```
┌──────────────────────────────────────────────────────────────────────┐
│  📝 Quizzes                                                          │
│                                                                      │
│  Select a generated quiz or create one from your docs.               │
│                                                                      │
│  ┌────────────────────┐  ┌────────────────────┐  ┌────────────────┐  │
│  │ 🐍 Python Basics   │  │ 🤖 AI Concepts     │  │ ➕ Create New  │  │
│  │ 20 Questions       │  │ 15 Questions       │  │ From Doc       │  │
│  │ Difficulty: Easy   │  │ Difficulty: Hard   │  │                │  │
│  │ [ Start Quiz ]     │  │ [ Start Quiz ]     │  │ [ + Create ]   │  │
│  └────────────────────┘  └────────────────────┘  └────────────────┘  │
│                                                                      │
│  Your Past Results                                                   │
│  • Python Basics: 80% (Passed) - Dec 20 [ View Cert ]                │
│  • History: 40% (Failed) - Dec 18 [ Retry ]                          │
└──────────────────────────────────────────────────────────────────────┘
```

## 7.2 Quiz Review Answers

```
┌──────────────────────────────────────────────────────────────────────┐
│  < Back to Results       Review: Python Basics                       │
│                                                                      │
│  Question 1: What is a list?                                         │
│  [x] A mutable sequence (Correct)                                    │
│  [ ] An immutable sequence                                           │
│  ✅ You answered correctly.                                          │
│                                                                      │
│  Question 2: What is a tuple?                                        │
│  [x] A mutable sequence                                              │
│  [ ] An immutable sequence (Correct)                                 │
│  ❌ You answered incorrectly.                                        │
│  💡 Explanation: Tuples are immutable in Python...                   │
│                                                                      │
└──────────────────────────────────────────────────────────────────────┘
```

---

# 8. User Profile & Settings

## 8.1 Profile Edit

```
┌──────────────────────────────────────────────────────────────────────┐
│  Profile Settings                                                    │
│                                                                      │
│  [ Upload Photo ]  ( JP )                                            │
│                                                                      │
│  First Name                  Last Name                               │
│  [ John                  ]   [ Doe                   ]               │
│                                                                      │
│  Email Address (Read only)                                           │
│  [ john@example.com      ]                                           │
│                                                                      │
│  Job Title                   Bio                                     │
│  [ Developer             ]   [ Learning AI...        ]               │
│                                                                      │
│  [ Save Changes ]                                                    │
└──────────────────────────────────────────────────────────────────────┘
```

## 8.2 Security Settings

```
┌──────────────────────────────────────────────────────────────────────┐
│  Security                                                            │
│                                                                      │
│  Change Password                                                     │
│  Current: [ ........... ]                                            │
│  New:     [ ........... ]                                            │
│  Confirm: [ ........... ]                                            │
│  [ Update Password ]                                                 │
│                                                                      │
│  Two-Factor Authentication (2FA)                                     │
│  Status: Disabled                                                    │
│  [ Enable 2FA ]                                                      │
│                                                                      │
│  Active Sessions                                                     │
│  • Windows 11 - Chrome - Now                                         │
│  • iPhone 13 - Safari - 2h ago       [ Log out all ]                 │
└──────────────────────────────────────────────────────────────────────┘
```

## 8.3 Notification Preferences

```
┌──────────────────────────────────────────────────────────────────────┐
│  Notifications                                                       │
│                                                                      │
│  Email Notifications                                                 │
│  [x] Product Updates                                                 │
│  [x] Quiz Results                                                    │
│  [ ] Weekly Learning Digest                                          │
│                                                                      │
│  Push Notifications                                                  │
│  [x] New Message from AI                                             │
│  [x] Document Processing Complete                                    │
│                                                                      │
│  [ Save Preferences ]                                                │
└──────────────────────────────────────────────────────────────────────┘
```

---

# 9. Subscription & Billing

## 9.1 Checkout Page

```
┌──────────────────────────────────────────────────────────────────────┐
│  Upgrade to Pro                                                      │
│                                                                      │
│  Order Summary                                                       │
│  Pro Plan (Monthly) .................................. $9.99         │
│  Tax ................................................. $1.00         │
│  Total ............................................... $10.99        │
│                                                                      │
│  Payment Details                                                     │
│  [ Card Icon ]                                                       │
│  Card Number: [ 4242 4242 4242 4242 ]                                │
│  Expiry: [ MM / YY ]   CVC: [ 123 ]                                  │
│  Zip Code: [ 10001 ]                                                 │
│                                                                      │
│  [ Pay $10.99 ]                                                      │
│                                                                      │
│  🔒 Secure payment via Stripe                                        │
└──────────────────────────────────────────────────────────────────────┘
```

## 9.2 Invoice View

```
┌──────────────────────────────────────────────────────────────────────┐
│  INVOICE #INV-2024-001                                [ Print ]      │
│                                                                      │
│  To:                   From:                                         │
│  John Doe              AI Smart Skill Coach LLC                      │
│  123 Main St           Tech Park, CA                                 │
│                                                                      │
│  Date: Dec 28, 2024                                                  │
│                                                                      │
│  Item                  Qty      Price      Total                     │
│  -------------------------------------------------                   │
│  Pro Plan (Monthly)     1       $9.99      $9.99                     │
│                                                                      │
│  Subtotal: $9.99                                                     │
│  Tax: $0.00                                                          │
│  TOTAL: $9.99                                                        │
│                                                                      │
│  PAID with Visa ending 4242                                          │
└──────────────────────────────────────────────────────────────────────┘
```

---

*Document Version: 3.0 | 25+ Screens | Comprehensive Web Flows*
