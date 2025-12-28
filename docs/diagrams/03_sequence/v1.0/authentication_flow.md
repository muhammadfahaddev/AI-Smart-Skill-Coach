# Sequence Diagram - Authentication Flow
## AI Smart Skill Coach - v1.0

```mermaid
sequenceDiagram
    autonumber
    participant U as User
    participant F as Frontend
    participant A as API Server
    participant D as Database
    participant E as Email Service

    rect rgb(240, 248, 255)
        Note over U,E: Registration Flow
        U->>F: Enter registration details
        F->>A: POST /api/auth/register
        A->>A: Validate input
        A->>A: Hash password (bcrypt)
        A->>D: Create user record
        D-->>A: User created
        A->>E: Send verification email
        A-->>F: Success response
        F-->>U: Show verification message
    end

    rect rgb(255, 248, 240)
        Note over U,E: Email Verification
        U->>E: Click verification link
        E->>F: Redirect to verify page
        F->>A: POST /api/auth/verify-email
        A->>D: Update email_verified = true
        A-->>F: Verification success
        F-->>U: Email verified
    end

    rect rgb(240, 255, 240)
        Note over U,D: Login Flow
        U->>F: Enter credentials
        F->>A: POST /api/auth/login
        A->>D: Get user by email
        D-->>A: User record
        A->>A: Verify password hash
        A->>A: Generate JWT tokens
        A->>D: Store refresh token
        A-->>F: Access + Refresh tokens
        F->>F: Store tokens securely
        F-->>U: Redirect to dashboard
    end

    rect rgb(255, 240, 245)
        Note over U,D: Token Refresh
        F->>A: POST /api/auth/refresh
        A->>D: Validate refresh token
        A->>A: Generate new access token
        A-->>F: New access token
    end
```

---

## Authentication Security

| Security Measure | Implementation |
|------------------|----------------|
| Password Storage | bcrypt with cost factor 12 |
| Token Type | JWT (RS256) |
| Access Token TTL | 15 minutes |
| Refresh Token TTL | 7 days |
| Email Verification | Required before full access |
