# Deployment Guide
## AI Smart Skill Coach

---

| Document Information | |
|---------------------|---------------------------|
| **Document ID** | OPS-DEPLOY-AISSC-001 |
| **Version** | 1.0 |
| **Date** | December 28, 2024 |
| **Status** | Draft |

---

# 1. Prerequisites
- Docker & Docker Compose installed.
- Azure CLI authenticated.
- Node.js 18+ & Python 3.10+.
- Access to GitHub Repository.

---

# 2. Local Development Setup

## 2.1 Clone & Env
```bash
git clone https://github.com/org/ai-smart-skill-coach.git
cd ai-smart-skill-coach
cp .env.example .env
```

## 2.2 Start Services using Docker
```bash
docker-compose up -d --build
# Starts: MySQL, Redis, ChromaDB, Backend API
```

## 2.3 Frontend Setup
```bash
cd web-app
npm install
npm run dev
# Running on http://localhost:3000
```

---

# 3. Production Deployment (Azure)

## 3.1 CI/CD Pipeline (GitHub Actions)
- **Trigger:** Push to `main` branch.
- **Steps:**
  1. **Test:** Run PyTest & Jest.
  2. **Build:** Build Docker images.
  3. **Push:** Push to Azure Container Registry (ACR).
  4. **Deploy:** Update Azure App Service / AKS.

## 3.2 Manual Deployment Steps
1. **Database Migration:**
   ```bash
   alembic upgrade head
   ```
2. **Static Assets:**
   ```bash
   npm run build
   # Upload to Azure CDN
   ```
3. **Environment Variables:**
   - Update App Service configuration with Prod secrets.

---

# 4. Rollback Strategy
- **Database:** Point-in-time recovery via Azure Backup (daily).
- **Code:** Revert to previous Docker image tag in App Service.

---

*Document Version: 1.0 | Last Updated: December 28, 2024*
