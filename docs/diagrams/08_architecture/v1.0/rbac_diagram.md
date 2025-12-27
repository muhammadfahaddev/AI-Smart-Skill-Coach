# RBAC (Role-Based Access Control) Diagram
## AI Smart Skill Coach - v1.0

```mermaid
flowchart TB
    subgraph Hierarchy["ROLE HIERARCHY"]
        SA["🔐 SUPER_ADMIN<br/>All permissions + System config"]
        A["👔 ADMIN<br/>User management + Content + Reports"]
        P["⭐ PREMIUM USER<br/>Unlimited + Priority Support"]
        PR["💎 PRO USER<br/>Unlimited docs, 3 certs/month"]
        F["👤 FREE USER<br/>5 docs, 50 Q/day, Basic"]
    end

    SA --> A
    A --> P
    A --> PR
    A --> F

    subgraph Matrix["PERMISSION MATRIX"]
        direction LR
        subgraph Free["FREE"]
            F1["5 docs max"]
            F2["50 Q/day"]
            F3["Basic quizzes"]
        end
        subgraph Pro["PRO"]
            P1["∞ docs"]
            P2["∞ questions"]
            P3["All quizzes"]
            P4["3 certs/month"]
        end
        subgraph Premium["PREMIUM"]
            PM1["∞ everything"]
            PM2["Priority Support"]
        end
        subgraph Admin["ADMIN"]
            A1["User Management"]
            A2["Content Control"]
            A3["Reports Access"]
        end
        subgraph Super["SUPER_ADMIN"]
            S1["System Config"]
            S2["All above"]
        end
    end
```

## Permission Details

| Permission | FREE | PRO | PREMIUM | ADMIN | SUPER_ADMIN |
|------------|------|-----|---------|-------|-------------|
| Upload Documents | 5 max | ∞ | ∞ | ∞ | ∞ |
| AI Questions | 50/day | ∞ | ∞ | ∞ | ∞ |
| Quizzes | Basic | All | All | All | All |
| Certificates | ✗ | 3/month | ∞ | ∞ | ∞ |
| Priority Support | ✗ | ✗ | ✓ | ✓ | ✓ |
| User Management | ✗ | ✗ | ✗ | ✓ | ✓ |
| System Config | ✗ | ✗ | ✗ | ✗ | ✓ |

## Role Inheritance

```
SUPER_ADMIN
    └── ADMIN
        ├── PREMIUM USER
        ├── PRO USER
        └── FREE USER
```
