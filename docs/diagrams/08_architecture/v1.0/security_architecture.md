# Security Architecture Diagram
## AI Smart Skill Coach - v1.0

```mermaid
flowchart TB
    subgraph Identity["🔐 Identity Layer"]
        OAuth["OAuth2/OIDC"]
        JWT["JWT Tokens"]
        MFA["MFA (Optional)"]
        RBAC["RBAC Access"]
    end

    subgraph Network["🌐 Network Layer"]
        WAF["WAF Firewall"]
        TLS["TLS 1.3"]
        Rate["Rate Limiting"]
        Gateway["API Gateway"]
    end

    subgraph App["📱 Application Layer"]
        Input["Input Validation"]
        CSRF["CSRF Protection"]
        XSS["XSS Prevention"]
        Prompt["Prompt Injection Guard"]
    end

    subgraph Data["💾 Data Layer"]
        Encrypt["AES-256 Encryption"]
        Hash["bcrypt Hashing"]
        Mask["Data Masking"]
        Audit["Audit Logging"]
    end

    subgraph Compliance["📋 Compliance"]
        GDPR["GDPR"]
        PCI["PCI DSS"]
        Privacy["Privacy by Design"]
    end

    User["👤 User"] --> WAF
    WAF --> TLS
    TLS --> Rate
    Rate --> Gateway
    Gateway --> OAuth
    OAuth --> JWT
    JWT --> RBAC
    RBAC --> Input
    Input --> App
    App --> Encrypt
    Encrypt --> Data

    Data --> Compliance

    style Identity fill:#e8f5e9
    style Network fill:#e3f2fd
    style App fill:#fff3e0
    style Data fill:#fce4ec
```

---

## Security Controls

| Layer | Controls |
|-------|----------|
| Identity | OAuth2, JWT, MFA, RBAC |
| Network | WAF, TLS 1.3, Rate Limiting |
| Application | Input Validation, CSRF, XSS, Prompt Guard |
| Data | AES-256, bcrypt, Masking, Audit Logs |
| Compliance | GDPR, PCI DSS |
