# Mobile Application Wireframes
## AI Smart Skill Coach

---

| Document Information | |
|---------------------|---------------------------|
| **Document ID** | UIUX-WF-MOB-001 |
| **Version** | 3.0 |
| **Date** | December 28, 2024 |
| **Status** | Draft |
| **Platform** | iOS / Android (375x812) |
| **Author** | Senior UI/UX Designer |

---

# Table of Contents

1. [Navigation Structure](#1-navigation-structure)
2. [Onboarding & Auth](#2-onboarding--auth)
3. [Main Application](#3-main-application)
4. [Document Interaction](#4-document-interaction)
5. [Chat Experience](#5-chat-experience)
6. [Quizzes](#6-quizzes)
7. [Profile & Settings](#7-profile--settings)

---

# 1. Navigation Structure

## 1.1 Visual Hierarchy

```
[ Top App Bar: Title, Notifications, Avatar ]
   |
[ Content Area / Scroll View ]
   |
[ Bottom Navigation Bar: Home, Docs, Chat, Quiz, Profile ]
```

---

# 2. Onboarding & Auth

## 2.1 Splash Screen

```
┌─────────────────────────┐
│                         │
│                         │
│          🤖             │
│         AISSC           │
│                         │
│      Loading... 🔄      │
└─────────────────────────┘
```

## 2.2 Onboarding (Slide 1/3)

```
┌─────────────────────────┐
│ [Skip]                  │
│      [ Artwork ]        │
│                         │
│    Prepare Smarter      │
│                         │
│ Chat with your PDFs to  │
│ learn 10x faster.       │
│                         │
│      ● ○ ○              │
│      [ Next ]           │
└─────────────────────────┘
```

## 2.3 Login

```
┌─────────────────────────┐
│    Welcome Back!        │
│                         │
│  [ Email Address ]      │
│  [ Password      ]      │
│                         │
│  [    Login      ]      │
│                         │
│  Forgot Password?       │
│                         │
│  --- Or ---             │
│  [ Google ] [ Apple ]   │
│                         │
│  [ Create Account ]     │
└─────────────────────────┘
```

## 2.4 Sign Up

```
┌─────────────────────────┐
│    Create Account       │
│                         │
│  [ Full Name     ]      │
│  [ Email Address ]      │
│  [ Password      ]      │
│                         │
│  [x] I agree to Terms   │
│                         │
│  [   Sign Up     ]      │
└─────────────────────────┘
```

---

# 3. Main Application

## 3.1 Home Dashboard

```
┌─────────────────────────┐
│ 🤖 AISSC           🔔 👤│
├─────────────────────────┤
│ 👋 Hi John!             │
│ 🔥 5 Day Streak         │
│                         │
│ Quick Actions           │
│ [📤 Upload] [❓ Ask ]   │
│                         │
│ Recent Docs             │
│ ┌─────────────────────┐ │
│ │ 📄 ML_Basics.pdf    │ │
│ │ 🕒 2h ago           │ │
│ └─────────────────────┐ │
│ ┌─────────────────────┐ │
│ │ 📄 History.pdf      │ │
│ │ 🕒 5h ago           │ │
│ └─────────────────────┐ │
│                         │
│ Daily Challenge         │
│ ┌─────────────────────┐ │
│ │ ⚡ Python Quiz      │ │
│ │ [ Start Now ]       │ │
│ └─────────────────────┐ │
├─────────────────────────┤
│ 🏠  📄  💬  📝  👤  │
└─────────────────────────┘
```

## 3.2 Notification Center

```
┌─────────────────────────┐
│ < Notifications     🗑️  │
├─────────────────────────┤
│ Today                   │
│ ┌─────────────────────┐ │
│ │ 🤖 AI Coach         │ │
│ │ Your quiz results...│ │
│ │ 2m ago              │ │
│ └─────────────────────┐ │
│ ┌─────────────────────┐ │
│ │ ✅ System           │ │
│ │ Doc processing done │ │
│ │ 1h ago              │ │
│ └─────────────────────┐ │
│                         │
│ Yesterday               │
│ ...                     │
└─────────────────────────┘
```

---

# 4. Document Interaction

## 4.1 Documents List

```
┌─────────────────────────┐
│ Documents            🔍 │
├─────────────────────────┤
│  [All] [Processed]      │
│                         │
│ 📄 ML_Basics.pdf        │
│    2.4MB • Ready        │
│    [Chat] [⋮]           │
│                         │
│ 📄 Bio_Notes.docx       │
│    1.2MB • Ready        │
│    [Chat] [⋮]           │
│                         │
│ 📄 Failed_Doc.txt       │
│    Error • Retry?       │
│    [Retry] [🗑️]         │
└─────────────────────────┘
```

## 4.2 Document Actions (Bottom Sheet)

```
┌─────────────────────────┐
│        [Handle]         │
│    ML_Basics.pdf        │
│  ─────────────────────  │
│  💬 Chat with Doc       │
│  ✏️ Rename              │
│  ℹ️ Details             │
│  🔗 Share               │
│  🗑️ Delete              │
└─────────────────────────┘
```

---

# 5. Chat Experience

## 5.1 Chat List (History)

```
┌─────────────────────────┐
│ Chats                ➕ │
├─────────────────────────┤
│ Today                   │
│ 💬 ML Questions         │
│    "What is SVM?"       │
│                         │
│ Yesterday               │
│ 💬 Bio Layouts          │
│    "Explain cells"      │
│                         │
│ 💬 Python Help          │
│    "Code for loops"     │
└─────────────────────────┘
```

## 5.2 Active Chat

```
┌─────────────────────────┐
│ < ML_Basics.pdf      📋 │
├─────────────────────────┤
│ [Bot]                   │
│ SVM stands for Support  │
│ Vector Machine...       │
│ 📄 Page 5 [Link]        │
│                         │
│           [User]        │
│        Using Kernels?   │
│                         │
│ [Bot]                   │
│ Yes, kernels allow...   │
│                         │
│                         │
├─────────────────────────┤
│ [📎] [ Message... ] [➤] │
└─────────────────────────┘
```

---

# 6. Quizzes

## 6.1 Quiz Question

```
┌─────────────────────────┐
│ < Python Quiz (1/10)    │
│ ⏱️ 09:45               │
├─────────────────────────┤
│ Which keyword defines   │
│ a function?             │
│                         │
│ ( ) func                │
│ (•) def                 │
│ ( ) function            │
│ ( ) define              │
│                         │
│                         │
│ [ Previous ] [ Next ]   │
└─────────────────────────┘
```

## 6.2 Quiz Results

```
┌─────────────────────────┐
│      🎉 Awesome!        │
│                         │
│      Score: 90%         │
│                         │
│    Passed: Yes ✅       │
│    Correct: 9/10        │
│                         │
│ [ Review Answers ]      │
│ [ Download Cert 🏆 ]    │
│                         │
│ [ Back to Home ]        │
└─────────────────────────┘
```

---

# 7. Profile & Settings

## 7.1 Settings Menu

```
┌─────────────────────────┐
│ < Settings              │
├─────────────────────────┤
│ Account                 │
│  👤 Edit Profile  >     │
│  🔒 Change Password >   │
│                         │
│ App Settings            │
│  🔔 Notifications >     │
│  🌙 Dark Mode    [O]    │
│  🌐 Language      >     │
│                         │
│ Support                 │
│  ❓ Help Center   >     │
│  📝 Send Feedback >     │
│                         │
│ [ Log Out ]             │
│ Version 1.0.0           │
└─────────────────────────┘
```

## 7.2 Edit Profile

```
┌─────────────────────────┐
│ < Edit Profile          │
├─────────────────────────┤
│    [ Avatar ] 📷        │
│                         │
│ Name                    │
│ [ John Doe        ]     │
│                         │
│ Job Title               │
│ [ Product Mgr     ]     │
│                         │
│ [ Save Changes ]        │
└─────────────────────────┘
```

---
*Document Version: 3.0 | 18 Screens | Complete Mobile Flows*
