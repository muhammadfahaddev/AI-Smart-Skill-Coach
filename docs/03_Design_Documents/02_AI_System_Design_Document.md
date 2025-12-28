# AI System Design Document (AI-SDD)
## AI Smart Skill Coach

---

| Document Information | |
|---------------------|---------------------------|
| **Document ID** | AI-SDD-AISSC-001 |
| **Version** | 2.0 |
| **Date** | December 28, 2024 |
| **Status** | ✅ Implemented |
| **Author** | Senior Full Stack AI Engineer |

---

# Table of Contents

1. [Overview & Motivation](#1-overview--motivation)
2. [AI Requirements](#2-ai-requirements)
3. [AI Architecture](#3-ai-architecture)
4. [RAG Pipeline Design](#4-rag-pipeline-design)
5. [Fine-Tuning Strategy](#5-fine-tuning-strategy)
6. [Model Selection](#6-model-selection)
7. [Data Pipeline Design](#7-data-pipeline-design)
8. [Personalization Engine](#8-personalization-engine)
9. [AI Guardrails & Safety](#9-ai-guardrails--safety)
10. [Monitoring & Evaluation](#10-monitoring--evaluation)
11. [Deployment Strategy](#11-deployment-strategy)
12. [Cost Optimization](#12-cost-optimization)

---

# 1. Overview & Motivation

## 1.1 Problem Statement

Traditional e-learning platforms face:

| Problem | Impact |
|---------|--------|
| Generic AI Responses | Low relevance to user's materials |
| AI Hallucinations | Wrong/misleading information |
| No Personalization | One-size-fits-all learning |
| Context Limitations | Limited document understanding |

## 1.2 AI Solution

| Component | Technology | Benefit |
|-----------|------------|---------|
| **RAG Pipeline** | LangChain + ChromaDB | Accurate, document-based answers |
| **Fine-Tuned LLM** | Mistral 7B + LoRA | Domain-specific expertise |
| **Personalization** | ML Analytics | Adaptive learning paths |
| **Guardrails** | Safety filters | Prevent harmful outputs |

## 1.3 Success Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Answer Accuracy | > 85% | Human evaluation |
| Hallucination Rate | < 5% | Fact-checking |
| Response Latency | < 5s | P95 |
| User Satisfaction | > 4.5/5 | NPS surveys |

---

# 2. AI Requirements

## 2.1 Functional Requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| AI-FR-001 | Answer questions from user's documents | P0 |
| AI-FR-002 | Cite sources in responses | P0 |
| AI-FR-003 | Handle multi-turn conversations | P0 |
| AI-FR-004 | Detect weak areas from chat history | P1 |
| AI-FR-005 | Generate personalized recommendations | P1 |
| AI-FR-006 | Support multiple domains | P1 |

## 2.2 Non-Functional Requirements

| ID | Requirement | Target |
|----|-------------|--------|
| AI-NFR-001 | Response time | < 5 seconds |
| AI-NFR-002 | Concurrent users | 1,000+ |
| AI-NFR-003 | Document processing | < 30 seconds |
| AI-NFR-004 | Uptime | 99.9% |
| AI-NFR-005 | Cost per query | < $0.01 |

---

# 3. AI Architecture

## 3.1 High-Level Architecture

![AI System Architecture](../diagrams/09_ai/v1.0/ai_system_architecture.png)

## 3.2 Component Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                        AI ENGINE LAYER                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    LANGCHAIN ORCHESTRATOR                     │   │
│  └───────────────────────────┬─────────────────────────────────┘   │
│                              │                                      │
│         ┌────────────────────┼────────────────────┐                │
│         │                    │                    │                 │
│  ┌──────▼──────┐     ┌───────▼──────┐    ┌───────▼──────┐         │
│  │   INPUT     │     │    RAG       │    │   OUTPUT     │         │
│  │  GUARDRAILS │     │   PIPELINE   │    │  GUARDRAILS  │         │
│  └──────┬──────┘     └───────┬──────┘    └───────┬──────┘         │
│         │                    │                   │                  │
│         │            ┌───────▼──────┐           │                  │
│         │            │   RETRIEVER  │           │                  │
│         │            │  (ChromaDB)  │           │                  │
│         │            └───────┬──────┘           │                  │
│         │                    │                   │                  │
│         │            ┌───────▼──────┐           │                  │
│         │            │  LLM CALL    │           │                  │
│         └───────────▶│  (Gemini)    │◀──────────┘                  │
│                      └──────────────┘                               │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

## 3.3 Technology Stack (Implemented)

| Component | Technology | Status |
|-----------|------------|--------|
| Orchestration | Custom Python Pipeline | ✅ Done |
| RAG LLM | Groq (llama-3.3-70b-versatile) | ✅ Done |
| Embeddings | sentence-transformers/all-MiniLM-L6-v2 | ✅ Done |
| Vector DB | ChromaDB (local) + Pinecone (cloud) | ✅ Done |
| Cache | File-based + Semantic Cache | ✅ Done |
| Security | PromptShield + PIIMasker + ContentFilter | ✅ Done |
| Evaluation | RAGAS (Faithfulness, Relevancy) | ✅ Done |

---

# 4. RAG Pipeline Design

## 4.1 Pipeline Overview

![Document Ingestion Pipeline](../diagrams/09_ai/v1.0/document_ingestion_pipeline.png)

## 4.2 Indexing Workflow (Offline)

| Step | Process | Technology |
|------|---------|------------|
| 1 | Document Upload | FastAPI |
| 2 | Validation | Pydantic (size, type) |
| 3 | Text Extraction | PyPDF2, pdfplumber |
| 4 | Chunking | RecursiveCharacterTextSplitter |
| 5 | Embedding | sentence-transformers |
| 6 | Vector Storage | ChromaDB |

### 4.2.1 Chunking Configuration

```python
chunking_config = {
    "chunk_size": 800,           # tokens
    "chunk_overlap": 150,        # tokens
    "separators": ["\n\n", "\n", ".", " "],
    "length_function": "tiktoken"
}
```

### 4.2.2 Embedding Configuration

```python
embedding_config = {
    "model": "sentence-transformers/all-mpnet-base-v2",
    "dimension": 768,
    "normalize": True,
    "batch_size": 32
}
```

## 4.3 Query Workflow (Online)

| Step | Process | Latency Target |
|------|---------|----------------|
| 1 | Query Input | - |
| 2 | Query Embedding | < 50ms |
| 3 | Vector Search (Top-K) | < 200ms |
| 4 | Re-ranking (Optional) | < 100ms |
| 5 | Context Assembly | < 10ms |
| 6 | LLM Generation | < 3s |
| 7 | Response Delivery | < 50ms |

### 4.3.1 Retrieval Configuration

```python
retrieval_config = {
    "top_k": 5,
    "similarity_metric": "cosine",
    "min_score_threshold": 0.7,
    "rerank": True,
    "rerank_model": "cross-encoder/ms-marco-MiniLM-L-6-v2"
}
```

## 4.4 Prompt Template

```
SYSTEM: You are an AI tutor for {domain}. 
Answer ONLY from the provided context below.
If the answer is not in the context, say "I don't have this information."
Always cite the source document and page number.

CONTEXT:
{retrieved_chunks}

SOURCES:
{source_metadata}

CONVERSATION HISTORY:
{chat_history}

USER QUESTION: {user_question}

Provide a clear, accurate answer with source citations.
```

---

# 5. Fine-Tuning Strategy

## 5.1 Hybrid Approach

| Use Case | Model | Fine-Tuning |
|----------|-------|-------------|
| RAG Q&A (90%) | Gemini 1.5 Flash | ❌ No |
| Domain Expert (10%) | Mistral 7B | ✅ LoRA |

## 5.2 LoRA Configuration

```python
lora_config = {
    "r": 32,                    # rank
    "lora_alpha": 64,           # scaling factor
    "lora_dropout": 0.05,
    "target_modules": ["q_proj", "k_proj", "v_proj", "o_proj"],
    "bias": "none"
}
```

## 5.3 Training Configuration

```python
training_config = {
    "per_device_batch_size": 4,
    "gradient_accumulation_steps": 8,
    "num_epochs": 3,
    "learning_rate": 2e-4,
    "warmup_ratio": 0.03,
    "lr_scheduler": "cosine",
    "fp16": True,
    "max_length": 2048
}
```

## 5.4 Domain Adapters

| Domain | Adapter | Training Data |
|--------|---------|---------------|
| IT & Programming | it_adapter.bin | 20,000 Q&A pairs |
| Medical | medical_adapter.bin | 50,000 verified pairs |
| Business | business_adapter.bin | 15,000 Q&A pairs |
| Academic | academic_adapter.bin | 30,000 curriculum pairs |

## 5.5 Adapter Selection Flow

```
User Query → Domain Detection → Load Adapter → Generate Response
                    ↓
           IT? → load(it_adapter)
           Medical? → load(medical_adapter)
           Business? → load(business_adapter)
           Default? → use(base_model)
```

---

# 6. Model Selection

## 6.1 Primary Models

| Model | Use Case | Context | Cost |
|-------|----------|---------|------|
| **Gemini 1.5 Flash** | RAG Q&A | 1M tokens | Free tier |
| **Gemini 1.5 Pro** | Complex Analysis | 2M tokens | Pay-per-use |

## 6.2 Fine-Tuning Models

| Model | Size | Use Case | License |
|-------|------|----------|---------|
| **Mistral 7B** | 7B | General Fine-Tune | Apache 2.0 |
| **CodeLlama** | 7B | IT Domain | Llama 2 |
| **BioMistral** | 7B | Medical Domain | Apache 2.0 |

## 6.3 Embedding Models

| Model | Dimensions | Speed | Quality |
|-------|------------|-------|---------|
| all-MiniLM-L6-v2 | 384 | Fast | Good |
| **all-mpnet-base-v2** | 768 | Medium | Best |

---

# 7. Data Pipeline Design

## 7.1 Document Processing Pipeline

| Stage | Input | Output | Technology |
|-------|-------|--------|------------|
| Upload | File (PDF/DOCX) | Blob URL | Azure Blob |
| Extract | Blob | Raw Text | PyPDF2, pdfplumber |
| Clean | Raw Text | Clean Text | Regex, NLTK |
| Chunk | Clean Text | Chunks (800 tokens) | LangChain |
| Embed | Chunks | Vectors (768 dims) | sentence-transformers |
| Store | Vectors | Vector IDs | ChromaDB |

## 7.2 Training Data Pipeline

| Stage | Description |
|-------|-------------|
| Collection | Gather domain Q&A pairs |
| Cleaning | Remove duplicates, fix formatting |
| Validation | Expert review for accuracy |
| Formatting | Convert to Alpaca/ShareGPT format |
| Splitting | 80% train, 10% val, 10% test |

## 7.3 Data Format (Alpaca)

```json
{
  "instruction": "Explain the concept of polymorphism in OOP",
  "input": "",
  "output": "Polymorphism is a fundamental OOP concept that allows objects of different classes to be treated as objects of a common base class..."
}
```

---

# 8. Personalization Engine

## 8.1 Architecture

```
User Interactions → Analytics Engine → ML Models → Recommendations
                          ↓
              ┌──────────────────────┐
              │  Progress Tracker    │
              │  Weak Area Detector  │
              │  Learning Path Gen   │
              └──────────────────────┘
```

## 8.2 Weak Area Detection

| Signal | Weight | Measurement |
|--------|--------|-------------|
| Incorrect Quiz Answers | 0.4 | Per topic |
| Repeated Questions | 0.3 | Same topic queries |
| Low Confidence Answers | 0.2 | AI confidence score |
| Time Spent | 0.1 | Extended time on topic |

## 8.3 Recommendation Engine

| Type | Algorithm | Output |
|------|-----------|--------|
| Content | Collaborative Filtering | Related documents |
| Topics | Content-Based | Weak area topics |
| Practice | Rule-Based | Targeted quizzes |

---

# 9. AI Guardrails & Safety

## 9.1 Input Guardrails

| Check | Implementation | Action |
|-------|----------------|--------|
| Toxicity | OpenAI Moderation API | Block |
| Prompt Injection | Pattern matching | Sanitize |
| Length | Max 4000 tokens | Truncate |
| Language | langdetect | Warn |

## 9.2 Output Guardrails

| Check | Implementation | Action |
|-------|----------------|--------|
| Harmful Content | Moderation API | Block |
| Hallucination | Source matching | Flag |
| Confidence | Self-assessment | Disclaimer |
| PII | Presidio | Redact |

## 9.3 Guardrail Configuration (Implemented)

```python
# security/prompt_shield.py - Injection Detection
PromptShield(
    strict_mode=False,
    injection_patterns=[...],  # 15+ patterns
    threat_levels=[SAFE, LOW, MEDIUM, HIGH, CRITICAL]
)

# security/pii_masker.py - Privacy Protection
PIIMasker(
    patterns=[email, phone, ssn, credit_card, cnic, ip]
)

# security/content_filter.py - Content Blocking
ContentFilter(
    categories=[SAFE, PROFANITY, HATE_SPEECH, VIOLENCE, MALICIOUS, SPAM]
)
```

---

# 10. Monitoring & Evaluation

## 10.1 Observability Stack

| Tool | Purpose |
|------|---------|
| **LangSmith** | LLM tracing, debugging |
| **Prometheus** | Metrics collection |
| **Grafana** | Dashboards |
| **Azure Monitor** | Cloud metrics |

## 10.2 Key Metrics

| Category | Metrics |
|----------|---------|
| **Latency** | P50, P95, P99 response time |
| **Quality** | Accuracy, hallucination rate |
| **Usage** | Queries/day, tokens/query |
| **Cost** | Cost/query, daily spend |
| **Errors** | Error rate, timeout rate |

## 10.3 RAG Evaluation (RAGAS) - ✅ Implemented

| Metric | Description | Implementation |
|--------|-------------|----------------|
| Faithfulness | Answer grounded in context | `evaluation/metrics/faithfulness.py` |
| Answer Relevancy | Answer addresses question | `evaluation/metrics/relevancy.py` |
| Context Relevancy | Retrieved context relevant | `evaluation/metrics/relevancy.py` |
| Golden Dataset | Test QA pairs | `evaluation/golden_dataset.py` |
| Batch Evaluator | Combined scoring | `evaluation/ragas_evaluator.py` |

## 10.4 Alerting Rules

| Alert | Condition | Severity |
|-------|-----------|----------|
| High Latency | P95 > 10s | Warning |
| Error Spike | Rate > 5% | Critical |
| Cost Overrun | Daily > budget | Warning |
| Model Down | Health fail | Critical |

---

# 11. Deployment Strategy

## 11.1 Deployment Modes

| Mode | Use Case | Strategy |
|------|----------|----------|
| Blue-Green | Major updates | Instant switch |
| Canary | New models | 5% → 25% → 100% |
| Shadow | Testing | No user impact |

## 11.2 Model Versioning

```
models/
├── production/
│   ├── rag_v1.2.0/
│   └── ft_mistral_v1.0.0/
├── staging/
│   └── rag_v1.3.0-beta/
└── archive/
    └── rag_v1.1.0/
```

## 11.3 Rollback Procedure

| Step | Action | Time |
|------|--------|------|
| 1 | Detect issue | < 5 min |
| 2 | Switch to previous | < 2 min |
| 3 | Notify team | Immediate |
| 4 | Analyze failure | 24 hours |

---

# 12. Cost Optimization

## 12.1 Token Usage Limits

| User Tier | Daily Tokens | Action |
|-----------|--------------|--------|
| Free | 50,000 | Block after limit |
| Pro | 500,000 | Warn at 80% |
| Premium | Unlimited | Monitor |

## 12.2 Caching Strategy

| Cache | TTL | Data |
|-------|-----|------|
| Embedding Cache | 7 days | Document vectors |
| Query Cache | 1 hour | Identical queries |
| Response Cache | 5 min | Repeated questions |

## 12.3 Cost Tracking

| Metric | Method |
|--------|--------|
| Tokens/Query | LangSmith |
| Cost/User | Daily aggregation |
| Model Split | GPT-4 vs Flash ratio |

---

*Document Version: 1.0 | Last Updated: December 27, 2024*
