# AI Requirements Specification (AI-RS)
## AI Smart Skill Coach

---

## Document Information

| Item | Details |
|------|---------|
| **Document Title** | AI Requirements Specification |
| **Version** | 2.0 |
| **Date** | December 28, 2024 |
| **Status** | ✅ Implemented |

---

# 1. RAG Pipeline Requirements

## 1.1 Document Processing Pipeline

### 1.1.1 Supported File Formats

| Format | Extension | Max Size | Processing |
|--------|-----------|----------|------------|
| PDF | .pdf | 10 MB | PyPDF2, pdfplumber |
| Word | .docx | 10 MB | python-docx |
| Text | .txt | 5 MB | Direct parsing |
| Markdown | .md | 5 MB | markdown parser |

### 1.1.2 Text Extraction Requirements

| Requirement ID | Description | Priority | Status |
|----------------|-------------|----------|--------|
| RAG-001 | Extract text from PDF with OCR fallback | High | ✅ Done |
| RAG-002 | Preserve document structure (headings, lists) | Medium | ✅ Done |
| RAG-003 | Handle multi-column layouts | Medium | ✅ Done |
| RAG-004 | Extract tables as structured data | Low | Pending |

### 1.1.3 Chunking Strategy

```
┌─────────────────────────────────────────────────────────────┐
│                    CHUNKING PARAMETERS                       │
├─────────────────────────────────────────────────────────────┤
│  Chunk Size:        500-1000 tokens                          │
│  Chunk Overlap:     100-150 tokens                           │
│  Splitter:          RecursiveCharacterTextSplitter           │
│  Separators:        ["\n\n", "\n", ".", " "]                │
└─────────────────────────────────────────────────────────────┘
```

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Chunk Size | 500-1000 tokens | Balance between context and retrieval precision |
| Overlap | 100-150 tokens | Maintain context continuity |
| Min Chunk | 100 tokens | Avoid too small fragments |

---

## 1.2 Embedding Generation

### 1.2.1 Embedding Model Selection

| Model | Dimensions | Speed | Quality | Recommendation |
|-------|------------|-------|---------|----------------|
| sentence-transformers/all-MiniLM-L6-v2 | 384 | Fast | Good | Development |
| sentence-transformers/all-mpnet-base-v2 | 768 | Medium | Better | Production |
| OpenAI text-embedding-3-small | 1536 | API | Best | Premium |

### 1.2.2 Embedding Requirements

| Requirement ID | Description | Priority | Status |
|----------------|-------------|----------|--------|
| EMB-001 | Generate embeddings for all document chunks | High | ✅ Done |
| EMB-002 | Support batch embedding generation | High | ✅ Done |
| EMB-003 | Cache embeddings to avoid re-computation | Medium | ✅ Done |
| EMB-004 | Support embedding model hot-swapping | Low | Pending |

---

## 1.3 Vector Storage & Retrieval

### 1.3.1 Vector Database Selection

| Database | Type | Scalability | Features | Recommendation |
|----------|------|-------------|----------|----------------|
| ChromaDB | Embedded | Small-Medium | Simple, Fast | MVP/Development |
| Pinecone | Cloud | High | Managed, Scalable | Production |
| Weaviate | Self-hosted | High | Hybrid Search | Enterprise |

### 1.3.2 Retrieval Requirements

| Requirement ID | Description | Priority | Status |
|----------------|-------------|----------|--------|
| VEC-001 | Similarity search with configurable top-k | High | ✅ Done |
| VEC-002 | Metadata filtering (user_id, doc_id) | High | ✅ Done |
| VEC-003 | Hybrid search (semantic + keyword) | Medium | ✅ Done |
| VEC-004 | Maximum retrieval latency < 200ms | High | ✅ Done |

### 1.3.3 Retrieval Configuration

```
┌─────────────────────────────────────────────────────────────┐
│                  RETRIEVAL PARAMETERS                        │
├─────────────────────────────────────────────────────────────┤
│  Top-K Results:     5-10 chunks                              │
│  Similarity Metric: Cosine Similarity                        │
│  Min Score:         0.7 (70% similarity threshold)          │
│  Re-ranking:        Optional (Cross-Encoder)                │
└─────────────────────────────────────────────────────────────┘
```

---

## 1.4 Response Generation

### 1.4.1 LLM Selection

| Model | Provider | Context | Cost | Use Case | Status |
|-------|----------|---------|------|----------|--------|
| llama-3.3-70b-versatile | Groq | 32K | Free tier | General Q&A | ✅ Using |
| GPT-3.5-turbo | OpenAI | 16K | Low | Alternative | Available |
| GPT-4 | OpenAI | 128K | High | Complex reasoning | Available |
| Mistral 7B | Local | 8K | Free | Cost-effective | Available |

### 1.4.2 Prompt Engineering Requirements

| Requirement ID | Description | Priority |
|----------------|-------------|----------|
| LLM-001 | System prompt with RAG context injection | High |
| LLM-002 | Source citation in responses | High |
| LLM-003 | Fallback for out-of-context questions | Medium |
| LLM-004 | Multi-turn conversation context | Medium |

### 1.4.3 RAG Prompt Template

```
SYSTEM: You are an AI tutor for {domain}. Answer ONLY from the 
provided context. If the answer is not in the context, say 
"I don't have this information in your documents."

CONTEXT:
{retrieved_chunks}

USER QUESTION: {user_question}

Provide a clear, accurate answer with source citations.
```

---

# 2. Fine-Tuning Requirements

## 2.1 Base Model Selection

| Criteria | Requirement |
|----------|-------------|
| Model Size | 7B-13B parameters (balance of quality and cost) |
| Architecture | Transformer-based (Llama 2, Mistral) |
| License | Open-source or commercial with fine-tuning rights |
| Quantization | Support 4-bit/8-bit for inference optimization |

### 2.1.1 Recommended Models

| Model | Size | Advantage | Domain | Provider |
|-------|------|-----------|--------|----------|
| **Gemini 1.5 Flash** | - | Fast, cost-effective | General | Google AI Studio |
| **Gemini 1.5 Pro** | - | Best quality | Complex reasoning | Google AI Studio |
| Llama 2 7B | 7B | Best balance | General | Meta (Open) |
| Mistral 7B | 7B | Better performance | Technical | Mistral AI |
| CodeLlama | 7B | Code understanding | IT Domain | Meta (Open) |
| BioMistral | 7B | Medical knowledge | Medical Domain | HuggingFace |

### 2.1.2 Primary Recommendation: Google AI Studio

| Model | Context | Cost | Best For |
|-------|---------|------|----------|
| **Gemini 1.5 Flash** | 1M tokens | Free tier available | RAG, Q&A |
| **Gemini 1.5 Pro** | 2M tokens | Pay-per-use | Complex analysis |
| **Gemini 1.0 Pro** | 32K tokens | Low cost | Basic tasks |

---

## 2.2 Training Data Requirements

### 2.2.1 Data Format

```json
{
  "instruction": "Explain the concept of inheritance in OOP",
  "input": "",
  "output": "Inheritance is a fundamental OOP concept where..."
}
```

### 2.2.2 Data Volume Requirements

| Domain | Min Samples | Recommended | Quality |
|--------|-------------|-------------|---------|
| IT & Programming | 5,000 | 20,000 | Curated Q&A pairs |
| Medical | 10,000 | 50,000 | Expert-verified |
| Business | 5,000 | 15,000 | Industry-specific |
| Academic | 5,000 | 30,000 | Curriculum-aligned |

### 2.2.3 Data Quality Requirements

| Requirement ID | Description | Priority |
|----------------|-------------|----------|
| DATA-001 | Clean, grammatically correct responses | High |
| DATA-002 | Domain expert verification for technical content | High |
| DATA-003 | Balanced distribution across topics | Medium |
| DATA-004 | No copyrighted or sensitive content | High |

---

## 2.3 LoRA/PEFT Configuration

### 2.3.1 LoRA Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| r (rank) | 8-64 | Lower = faster, Higher = better quality |
| alpha | 16-128 | Scaling factor (typically 2x rank) |
| dropout | 0.05-0.1 | Regularization |
| target_modules | ["q_proj", "v_proj"] | Attention layers |

### 2.3.2 Training Configuration

```python
training_args = {
    "per_device_train_batch_size": 4,
    "gradient_accumulation_steps": 8,
    "num_train_epochs": 3,
    "learning_rate": 2e-4,
    "warmup_ratio": 0.03,
    "lr_scheduler_type": "cosine",
    "fp16": True,
    "logging_steps": 10,
    "save_strategy": "epoch"
}
```

### 2.3.3 Hardware Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| GPU VRAM | 16 GB | 24 GB |
| GPU Model | RTX 3090 | A100 40GB |
| RAM | 32 GB | 64 GB |
| Storage | 100 GB SSD | 500 GB NVMe |

---

## 2.4 Domain Adapter Management

### 2.4.1 Adapter Storage

| Requirement ID | Description | Priority |
|----------------|-------------|----------|
| ADAPT-001 | Store adapters in cloud storage (Azure Blob) | High |
| ADAPT-002 | Version control for adapter weights | Medium |
| ADAPT-003 | Hot-swapping adapters based on user domain | High |
| ADAPT-004 | Adapter performance metrics tracking | Medium |

### 2.4.2 Adapter Selection Flow

```
User Request → Detect Domain → Load Adapter → Generate Response
                    ↓
             IT? → it_adapter.bin
             Medical? → medical_adapter.bin
             Business? → business_adapter.bin
             Default? → base_adapter.bin
```

---

# 3. Model Performance Metrics

## 3.1 Response Quality Metrics

| Metric | Target | Measurement |
|--------|--------|-------------|
| Answer Accuracy | > 85% | Human evaluation sample |
| Hallucination Rate | < 5% | Fact-checking against sources |
| Relevance Score | > 0.8 | Semantic similarity to ideal answer |
| Source Citation Accuracy | > 95% | Correct page/section references |

## 3.2 Latency Requirements

| Operation | Target Latency | Max Latency |
|-----------|----------------|-------------|
| Document Upload & Processing | < 30 sec | 60 sec |
| Embedding Generation | < 5 sec | 10 sec |
| Vector Search | < 200 ms | 500 ms |
| LLM Response | < 3 sec | 8 sec |
| Total Q&A Response | < 5 sec | 15 sec |

## 3.3 Scalability Metrics

| Metric | Target |
|--------|--------|
| Concurrent Users | 1,000+ |
| Documents per User | 100+ |
| Queries per Minute | 500+ |
| Vector DB Size | 10M+ vectors |

---

# 4. Data Pipeline Requirements

## 4.1 Document Ingestion Pipeline

![Document Ingestion Pipeline](../diagrams/09_ai/v1.0/document_ingestion_pipeline.png)

## 4.2 Training Data Pipeline

| Stage | Description | Output |
|-------|-------------|--------|
| Collection | Gather domain-specific Q&A pairs | Raw dataset |
| Cleaning | Remove duplicates, fix formatting | Cleaned dataset |
| Validation | Expert review for accuracy | Validated dataset |
| Formatting | Convert to training format (Alpaca/ShareGPT) | Training-ready |
| Splitting | Train/Val/Test split (80/10/10) | Final datasets |

## 4.3 Model Serving Pipeline

| Component | Technology | Purpose |
|-----------|------------|---------|
| Model Registry | MLflow | Version tracking |
| Inference Server | vLLM / TGI | Fast inference |
| Load Balancer | Nginx | Request distribution |
| Cache | Redis | Response caching |
| Monitoring | Prometheus + Grafana | Performance tracking |

---

## 5. AI System Architecture

![AI System Architecture](../diagrams/09_ai/v1.0/ai_system_architecture.png)

---

# 6. AI Security Requirements

## 6.1 API Key Management

| Requirement ID | Description | Priority |
|----------------|-------------|----------|
| SEC-AI-001 | Store API keys in Azure Key Vault | High |
| SEC-AI-002 | Rotate API keys every 90 days | Medium |
| SEC-AI-003 | Per-user API key isolation | High |
| SEC-AI-004 | Rate limiting per API key | High |

## 6.2 Prompt Injection Prevention

| Attack Type | Prevention Strategy | Implementation |
|-------------|---------------------|----------------|
| Direct Injection | Input sanitization | Regex + allowlist |
| Indirect Injection | Context isolation | Separate system/user prompts |
| Jailbreaking | Output filtering | Post-response validation |
| Data Exfiltration | PII detection | Microsoft Presidio |

```python
# Prompt Injection Defense
def sanitize_input(user_input: str) -> str:
    # Remove potential injection patterns
    patterns = ["ignore previous", "disregard", "new instructions"]
    for pattern in patterns:
        user_input = user_input.replace(pattern, "")
    return user_input
```

## 6.3 Data Privacy

| Requirement ID | Description | Priority |
|----------------|-------------|----------|
| PRIV-001 | User documents isolated by user_id | High |
| PRIV-002 | No cross-user data leakage in vector search | High |
| PRIV-003 | PII anonymization in training data | High |
| PRIV-004 | Right to deletion (GDPR compliance) | High |

---

# 7. AI Guardrails & Content Safety

## 7.1 Input Guardrails

| Check | Implementation | Action |
|-------|----------------|--------|
| Toxicity Detection | OpenAI Moderation API | Block + log |
| Language Detection | langdetect | Warn if non-supported |
| Length Limits | Max 4000 tokens | Truncate + notify |
| Topic Classification | Zero-shot classifier | Route appropriately |

## 7.2 Output Guardrails

| Check | Implementation | Action |
|-------|----------------|--------|
| Hallucination Detection | Source citation validation | Flag uncertain |
| Harmful Content | OpenAI Moderation | Block + replace |
| Confidence Score | LLM self-assessment | Low confidence disclaimer |
| Factual Grounding | RAG source matching | Require 70%+ match |

## 7.3 Guardrail Configuration

```python
guardrails_config = {
    "max_input_tokens": 4000,
    "max_output_tokens": 2000,
    "min_confidence_threshold": 0.7,
    "blocked_topics": ["illegal", "harmful", "adult"],
    "require_source_citation": True,
    "fallback_response": "Is sawal ka jawab aapke documents mein nahi mila."
}
```

---

# 8. Error Handling & Resilience

## 8.1 Failure Scenarios

| Scenario | Detection | Recovery Strategy |
|----------|-----------|-------------------|
| LLM API Timeout | 30 sec timeout | Retry 3x → fallback model |
| Vector DB Down | Health check | Use cached results |
| Embedding Failure | Exception catch | Queue for retry |
| Rate Limit Hit | 429 response | Exponential backoff |
| Invalid Response | JSON validation | Request regeneration |

## 8.2 Fallback Chain

```
Primary LLM (GPT-4) Failed?
    ↓
Secondary LLM (GPT-3.5) Failed?
    ↓
Local LLM (Mistral 7B) Failed?
    ↓
Graceful Error Message
```

## 8.3 Retry Configuration

```python
retry_config = {
    "max_retries": 3,
    "base_delay": 1,  # seconds
    "max_delay": 30,
    "exponential_base": 2,
    "retry_on": [429, 500, 502, 503, 504]
}
```

---

# 9. Cost Optimization

## 9.1 Token Usage Controls

| Control | Limit | Action |
|---------|-------|--------|
| Free User Daily Tokens | 50,000 | Block after limit |
| Pro User Daily Tokens | 500,000 | Warn at 80% |
| Premium User | Unlimited | Monitor only |
| Max Tokens per Request | 4,000 | Truncate context |

## 9.2 Caching Strategy

| Cache Level | TTL | Purpose |
|-------------|-----|---------|
| Embedding Cache | 7 days | Avoid re-embedding docs |
| Query Cache | 1 hour | Same question responses |
| Vector Search Cache | 5 min | Repeated searches |
| Session Context | 30 min | Multi-turn conversations |

## 9.3 Cost Tracking

| Metric | Tracking Method |
|--------|-----------------|
| Tokens per User | Daily aggregation |
| Cost per Query | Token count × price |
| Model Usage Split | GPT-4 vs 3.5 ratio |
| Monthly Projection | Rolling 7-day average |

---

# 10. Monitoring & Observability

## 10.1 LLM Observability Stack

| Tool | Purpose | Metrics |
|------|---------|---------|
| LangSmith | Trace debugging | Latency, tokens, errors |
| Prometheus | System metrics | CPU, memory, requests |
| Grafana | Dashboards | Real-time visualization |
| Azure Monitor | Cloud metrics | Availability, costs |

## 10.2 Key Metrics to Track

| Category | Metrics |
|----------|---------|
| **Performance** | P50/P95/P99 latency, throughput |
| **Quality** | Accuracy, hallucination rate, user feedback |
| **Cost** | Tokens/query, daily spend, cost/user |
| **Usage** | Queries/day, active users, document uploads |
| **Errors** | Error rate, timeout rate, retry rate |

## 10.3 Alerting Rules

| Alert | Condition | Severity |
|-------|-----------|----------|
| High Latency | P95 > 10 sec | Warning |
| Error Spike | Error rate > 5% | Critical |
| Cost Overrun | Daily cost > budget | Warning |
| Model Down | Health check fails | Critical |

---

# 11. Evaluation Framework

## 11.1 RAG Evaluation (RAGAS) - ✅ Implemented

| Metric | Description | Implementation |
|--------|-------------|----------------|
| Faithfulness | Answer grounded in context | `ai_engine/evaluation/metrics/faithfulness.py` |
| Answer Relevancy | Answer addresses question | `ai_engine/evaluation/metrics/relevancy.py` |
| Context Relevancy | Retrieved context relevant | `ai_engine/evaluation/metrics/relevancy.py` |
| Golden Dataset | Test QA pairs management | `ai_engine/evaluation/golden_dataset.py` |
| Batch Evaluator | Combined scoring & reports | `ai_engine/evaluation/ragas_evaluator.py` |

## 11.2 A/B Testing Framework

```
┌─────────────────────────────────────────┐
│              A/B TEST SETUP              │
├─────────────────────────────────────────┤
│  Control (50%): Current prompt/model    │
│  Variant (50%): New prompt/model        │
│                                          │
│  Metrics:                               │
│  - User satisfaction rating             │
│  - Response accuracy                    │
│  - Latency comparison                   │
│  - Cost per query                       │
└─────────────────────────────────────────┘
```

## 11.3 Continuous Evaluation

| Evaluation | Frequency | Method |
|------------|-----------|--------|
| Automated Tests | Daily | RAGAS on test set |
| Human Review | Weekly | Sample 100 queries |
| User Feedback | Ongoing | Thumbs up/down |
| Benchmark Suite | Monthly | Standard QA datasets |

---

# 12. Deployment Strategy

## 12.1 Deployment Modes

| Mode | Use Case | Rollout |
|------|----------|---------|
| Blue-Green | Major updates | Instant switch |
| Canary | New models | 5% → 25% → 100% |
| Feature Flag | Experiments | Per-user control |
| Shadow | Pre-production | No user impact |

## 12.2 Model Versioning

```
models/
├── production/
│   ├── llm_v2.1.0/
│   └── embeddings_v1.3.0/
├── staging/
│   └── llm_v2.2.0-beta/
└── archive/
    └── llm_v2.0.0/
```

## 12.3 Rollback Procedure

| Step | Action | Time |
|------|--------|------|
| 1 | Detect issue (automated/manual) | < 5 min |
| 2 | Switch to previous model version | < 2 min |
| 3 | Notify team | Immediate |
| 4 | Analyze failure | 24 hours |

---

*Document Version: 2.0 | Last Updated: December 28, 2024*
*Reviewed by: Senior Full Stack AI Engineer*
*Implementation Status: 10/10 Phases Complete*

