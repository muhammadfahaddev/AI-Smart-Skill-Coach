# Risk Assessment & Mitigation Strategy
## AI Smart Skill Coach

---

| Document Information | |
|---------------------|---------------------------|
| **Document ID** | PM-RISK-AISSC-002 |
| **Version** | 2.0 |
| **Date** | December 28, 2024 |
| **Status** | Active |
| **Author** | Senior Engineering Manager |

---

# 1. Executive Risk Summary

The project carries a **Medium-High** overall risk profile primarily driven by dependency on probabilistic AI models. While standard software components (Web/Mobile/DB) are low risk, the **RAG accuracy** and **LLM operation costs** represent significant variance vectors.

---

# 2. Strategic Risk Register

## 2.1 Technical Risks (Engineering Lead Ownership)

| ID | Risk Description | Probability | Impact | Sev. | Owner | Mitigation Strategy | Contingency Plan |
|----|------------------|------------|--------|------|-------|---------------------|------------------|
| **T1** | **Hallucinations:** AI generates plausible but false answers from user PDFs. | High (>60%) | Critical (5) | **20** | AI Lead | 1. Strict `temperature=0` settings.<br>2. Relevance score filtering (Threshold > 0.7).<br>3. Citation enforcement. | Fallback to "I don't know" response instead of guessing. Implement human feedback loop (RLHF). |
| **T2** | **Context Window Overflow:** Large documents exceed token limits. | Med (40%) | High (4) | **12** | Backend | 1. Implement sliding window chunking.<br>2. Use recursive summarization for long docs. | Force document splitting or limit PDF size to 50MB/200pgs. |
| **T3** | **Latency Spikes:** RAG pipeline takes >10s per query. | Med (30%) | High (4) | **10** | DevOps | 1. Cache frequent queries (Redis).<br>2. Use async/parallel processing.<br>3. Optimize vector index (HNSW). | switch to faster/smaller model (e.g., Gemini Flash vs Pro) dynamically. |

## 2.2 Operational & Business Risks (PM Ownership)

| ID | Risk Description | Probability | Impact | Sev. | Owner | Mitigation Strategy | Contingency Plan |
|----|------------------|------------|--------|------|-------|---------------------|------------------|
| **O1** | **API Cost Explosion:** Linear scaling of Token costs bankrupts the tier. | Med (40%) | Critical (5) | **15** | FinOps | 1. Implement strict rate limits per user tier.<br>2. Token usage dashboards/alerts.<br>3. Cache semantic duplicates. | Switch to Open Source model (Mistral/Llama) on self-hosted GPU. |
| **O2** | **Data Leakage:** User A sees User B's document context. | Low (10%) | Critical (5) | **10** | SecOps | 1. Row Level Security (RLS) in Vector DB.<br>2. Tenant isolation in metadata filters. | Immediate shutdown of RAG service. Rollback to last secure state. |

## 2.3 Schedule Risks (Scrum Master Ownership)

| ID | Risk Description | Probability | Impact | Sev. | Owner | Mitigation Strategy | Contingency Plan |
|----|------------------|------------|--------|------|-------|---------------------|------------------|
| **S1** | **Integration Hell:** AI component doesn't fit Backend API schema. | High (50%) | High (4) | **16** | Scrum M. | 1. API-First design (OpenAPI Spec).<br>2. Mock servers for frontend dev.<br>3. Daily integration builds. | Reduced scope: Drop "Quiz Generation" feature for launch. |

---

# 3. Risk Monitoring Process
- **Daily:** Blocker review in Standup (Scrum Master).
- **Weekly:** Risk Register review in Stakeholder sync (PM).
- **Trigger:** Any Severity > 15 triggers automatic Executive Escalation.

---

*Document Version: 2.0 | Status: Active Monitoring*
