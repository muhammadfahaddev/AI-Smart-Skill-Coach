# Resource Allocation & Budget Plan
## AI Smart Skill Coach

---

| Document Information | |
|---------------------|---------------------------|
| **Document ID** | PM-RES-AISSC-002 |
| **Version** | 2.0 |
| **Date** | December 28, 2024 |
| **Status** | Approved |
| **Author** | Senior Engineering Manager |

---

# 1. Human Capital Strategy

## 1.1 Team Composition & Utilization

| Role | Level | Count | Allocation | Key Responsibilities | Primary Skills Required |
|------|-------|-------|------------|----------------------|-------------------------|
| **Tech Lead / Architect** | Staff | 1 | 50% | System design, Code review, Technical decisions | Sys Design, Cloud Pattern, Python |
| **AI/ML Engineer** | Senior | 1 | 100% | RAG pipeline, Prompt Eng, Vector DB mgmt | LangChain, PyTorch, Embeddings |
| **Backend Engineer** | Mid | 2 | 100% | API Dev, DB Migrations, Auth Integration | FastAPI, SQL/SQLAlchemy, Docker |
| **Frontend Engineer** | Senior| 1 | 100% | Web App (Next.js) & Component Lib | React, TS, Tailwind, State Mgmt |
| **Mobile Engineer** | Mid | 1 | 100% | Flutter App (iOS/Android) | Dart, Flutter Bloc, Native Bridge |
| **QA Automation** | Mid | 1 | 100% | E2E Testing, CI/CD Integration | Playwright, PyTest, GitHub Actions |
| **Project Manager** | Senior| 1 | 50% | Agile ceremonies, Stakeholder comms | Jira, Agile, Risk Mgmt |

## 1.2 Onboarding Plan
- **Week 0:** Access provisioning (GitHub, Azure, Jira).
- **Week 1:** Domain Knowledge Transfer (KT) session on RAG & EdTech.
- **Week 1:** Env Setup (Docker local).

---

# 2. Infrastructure & Tooling Budget

## 2.1 Cloud Forecast (Azure) - Monthly

| Service | SKU / Configuration | Qty/Scale | Est. Cost (Mo) | Justification |
|---------|---------------------|-----------|----------------|---------------|
| **App Service (API)** | P1v3 (2 Core, 8GB) | 2 Instances | $250 | High CPU for text processing. |
| **App Service (Web)** | S1 (1 Core, 1.75GB) | 2 Instances | $150 | Standard web hosting. |
| **Database (MySQL)** | Flex Server (D4ds_v4)| 1 Instance | $280 | Production grade DB. |
| **AI/LLM API** | Gemini 1.5 Flash | ~5M Tokens | $350 | Based on 1k users * 50 queries/day. |
| **Vector DB** | Chroma (Hosted/K8s) | Standard | $150 | Vector storage & retrieval. |
| **Storage** | Blob (Hot/LRS) | 1 TB | $25 | PDF storage. |
| **Misc** | NAT Gateway, Bandwidth | - | $100 | Networking & Egress. |
| **TOTAL** | | | **~$1,305** | *Buffer +20% for scale spikes.* |

## 2.2 SaaS Tooling (Monthly)

| Tool | Plan | Seats | Cost |
|------|------|-------|------|
| **GitHub**| Team | 8 | $32 |
| **Jira** | Standard | 8 | $64 |
| **Slack** | Pro | 8 | $70 |
| **Figma** | Pro | 2 | $30 |
| **Sentinal**| (Security) | - | $100 |

---

# 3. Resource Gap Analysis

| Gap Identified | Risk Level | Mitigation Plan |
|----------------|------------|-----------------|
| **DevOps Specialist** | Med | Tech Lead will handle CI/CD setup initially. Consider contract hire for Launch. |
| **UI Designer** | Low | Frontend Dev to use component library (Shadcn/UI) to reduce design load. |

---

*Document Version: 2.0 | Budget Status: Within Limits*
