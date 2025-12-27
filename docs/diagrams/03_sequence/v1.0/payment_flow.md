# Sequence Diagram - Payment Flow
## AI Smart Skill Coach - v1.0

```mermaid
sequenceDiagram
    autonumber
    participant U as User
    participant F as Frontend
    participant A as API Server
    participant S as Stripe
    participant D as Database

    U->>F: Select subscription plan
    F->>A: POST /api/subscribe
    A->>S: Create Checkout Session
    S-->>A: Session URL
    A-->>F: Redirect URL
    F->>S: Redirect to Stripe
    U->>S: Enter payment details
    U->>S: Complete payment
    S-->>U: Redirect to success page
    
    Note over S,A: Webhook (async)
    S->>A: POST /webhook (payment.success)
    A->>A: Verify webhook signature
    A->>D: Update subscription status
    A->>D: Create payment record
    A-->>S: 200 OK
    
    F->>A: GET /api/subscription
    A->>D: Get subscription
    D-->>A: Active subscription
    A-->>F: Subscription details
    F-->>U: Show confirmation
```

---

## Payment Security

| Security Measure | Implementation |
|------------------|----------------|
| Card Data | Handled by Stripe (PCI DSS) |
| Webhook Verification | Stripe signature validation |
| Subscription Status | Webhook-based activation only |
