# Advanced Sprint Planning & Agile Governance
## AI Smart Skill Coach

---

| Document Information | |
|---------------------|---------------------------|
| **Document ID** | PM-SPRINT-AISSC-002 |
| **Version** | 2.0 |
| **Date** | December 28, 2024 |
| **Status** | Active |
| **Role** | Senior Scrum Master |
| **Cadence** | 2-Week Sprints |

---

# 1. Agile Framework Standards

## 1.1 Definition of Ready (DoR)
A user story is ready for a sprint only if:
1.  **Clear Description:** "As a [User], I want to [Action], so that [Benefit]."
2.  **Acceptance Criteria (AC):** Minimum 3 distinct pass/fail conditions listed.
3.  **Estimated:** Story points assigned (Fibonacci: 1, 2, 3, 5, 8).
4.  **Dependencies:** Identified and resolved.
5.  **UX:** Wireframes/Mocks attached (if UI involved).

## 1.2 Definition of Done (DoD)
A story is complete only when:
1.  Code merged to `develop` branch.
2.  All Unit Tests passed (>80% coverage).
3.  Peer Code Review completed (Apprv by 1 Senior).
4.  Documentation updated (API Swagger / Readme).
5.  QA Verification passed on Staging env.

## 1.3 Ceremonies
| Event | Duration | Attendees | Goal |
|-------|----------|-----------|------|
| **Sprint Planning** | 2 hrs | All | Commit to Sprint Backlog. |
| **Daily Standup** | 15 mins | Devs, SM | Blockers & Progress only. |
| **Sprint Review** | 1 hr | All + Stakeholders | Demo working software. |
| **Retrospective** | 45 mins | Devs, SM | Process improvement (Start/Stop/Continue). |

---

# 2. Detailed Sprint Roadmap

## Sprint 1: "Foundation & Ingestion" (Weeks 1-2)
**Theme:** Setting the rails and getting data in.

| ID | User Story | Pts | owner |
|----|------------|-----|-------|
| **BE-01** | As a Dev, I want to scaffold the FastAPI repo with Docker, so environment is consistent. | 3 | Backend |
| **AI-01** | As a System, I want to parse uploaded PDFs using PyPDF2, so text is available for embedding. | 5 | AI Eng |
| **AI-02** | As a System, I want to generate embeddings using `sentence-transformers`, so vector search works. | 5 | AI Eng |
| **DB-01** | As a Dev, I want to provision MySQL and ChromaDB in Azure, so persistence works. | 3 | DevOps |

## Sprint 2: "The Intelligent Core" (Weeks 3-4)
**Theme:** Making the AI answer questions.

| ID | User Story | Pts | owner |
|----|------------|-----|-------|
| **BE-05** | As a User, I can register/login via JWT, so my data is secure. | 5 | Backend |
| **AI-05** | As a System, I want to implement the RAG retrieval logic, so context is fetched. | 8 | AI Eng |
| **AI-06** | As a System, I want to integrate Gemini 1.5, so answers are generated from context. | 8 | AI Eng |
| **FE-01** | As a User, I can see a dashboard shell, so navigation is possible. | 3 | Frontend |

## Sprint 3: "Experience & Interaction" (Weeks 5-6)
**Theme:** Connecting frontend to backend.

| ID | User Story | Pts | owner |
|----|------------|-----|-------|
| **FE-05** | As a User, I want to drag-and-drop PDFs, so I can upload easily. | 5 | Frontend |
| **FE-06** | As a User, I want a chat interface with streaming text, so it feels responsive. | 8 | Frontend |
| **BE-10** | As a System, I want to enforce rate limits, so costs are controlled. | 5 | Backend |
| **MO-01** | As a Mobile User, I can login via Flutter app, so I can access on go. | 5 | Mobile |

## Sprint 4: "Polish & Monetize" (Weeks 7-8)
**Theme:** Making it production-ready.

| ID | User Story | Pts | owner |
|----|------------|-----|-------|
| **BE-15** | As a User, I want to pay for Pro subscription via Stripe, so I get unlimited access. | 8 | Backend |
| **AI-10** | As a System, I want to generate "Quiz Questions" from text, so users can practice. | 8 | AI Eng |
| **QA-01** | As a QA, I want to run Load Tests (1k users), so stability is handled. | 5 | QA |

---

*Document Version: 2.0 | Agreed by Team Lead*
