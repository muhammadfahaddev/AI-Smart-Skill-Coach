# Class Diagram
## AI Smart Skill Coach - v1.0

```mermaid
classDiagram
    direction TB
    
    %% User Domain
    class User {
        +UUID id
        +String email
        +String passwordHash
        +String name
        +String avatarUrl
        +Role role
        +Boolean emailVerified
        +DateTime createdAt
        +register()
        +login()
        +updateProfile()
        +changePassword()
    }

    class Subscription {
        +UUID id
        +UUID userId
        +PlanType planType
        +SubscriptionStatus status
        +String stripeCustomerId
        +String stripeSubscriptionId
        +DateTime currentPeriodEnd
        +activate()
        +cancel()
        +renew()
        +isPremium() Boolean
    }

    %% Document Domain
    class Document {
        +UUID id
        +UUID userId
        +String filename
        +String originalName
        +Long fileSize
        +String mimeType
        +DocumentStatus status
        +Int chunkCount
        +upload()
        +process()
        +delete()
    }

    class DocumentChunk {
        +UUID id
        +UUID documentId
        +Int chunkIndex
        +String content
        +String embeddingId
        +Int pageNumber
        +JSON metadata
        +generateEmbedding()
    }

    %% Chat Domain
    class ChatSession {
        +UUID id
        +UUID userId
        +String title
        +DateTime createdAt
        +addMessage()
        +getHistory()
    }

    class ChatMessage {
        +UUID id
        +UUID sessionId
        +MessageRole role
        +String content
        +JSON sources
        +Feedback feedback
        +addFeedback()
    }

    %% Quiz Domain
    class Quiz {
        +UUID id
        +String title
        +String description
        +Domain domain
        +Difficulty difficulty
        +Int passingScore
        +Int timeLimitMins
        +Boolean isPremium
        +getQuestions()
        +calculateScore()
    }

    class Question {
        +UUID id
        +UUID quizId
        +String questionText
        +QuestionType type
        +JSON options
        +String correctAnswer
        +String explanation
        +validateAnswer()
    }

    class QuizAttempt {
        +UUID id
        +UUID userId
        +UUID quizId
        +Decimal score
        +Boolean passed
        +JSON answers
        +Int timeTakenSecs
        +submit()
        +generateCertificate()
    }

    class Certificate {
        +UUID id
        +UUID userId
        +UUID quizId
        +UUID attemptId
        +String certificateNumber
        +Date issueDate
        +String pdfPath
        +generate()
        +verify()
    }

    %% AI/RAG Domain
    class RAGEngine {
        +processQuery(query)
        +similaritySearch(embedding)
        +buildContext(chunks)
        +generateResponse(context, query)
    }

    class VectorStore {
        +upsert(embedding, metadata)
        +query(embedding, topK)
        +delete(id)
    }

    %% Relationships
    User "1" --> "*" Document : uploads
    User "1" --> "0..1" Subscription : has
    User "1" --> "*" ChatSession : creates
    User "1" --> "*" QuizAttempt : attempts
    
    Document "1" --> "*" DocumentChunk : contains
    
    ChatSession "1" --> "*" ChatMessage : contains
    
    Quiz "1" --> "*" Question : has
    Quiz "1" --> "*" QuizAttempt : attempted
    
    QuizAttempt "1" --> "0..1" Certificate : generates
    
    RAGEngine --> VectorStore : uses
    RAGEngine --> DocumentChunk : retrieves

    %% Enums
    class Role {
        <<enumeration>>
        USER
        ADMIN
    }

    class PlanType {
        <<enumeration>>
        FREE
        BASIC
        PREMIUM
    }

    class DocumentStatus {
        <<enumeration>>
        PENDING
        PROCESSING
        COMPLETED
        FAILED
    }
```

---

## Domain Summary

| Domain | Classes | Description |
|--------|---------|-------------|
| User | User, Subscription | User management & subscriptions |
| Document | Document, DocumentChunk | Document upload & processing |
| Chat | ChatSession, ChatMessage | AI chat functionality |
| Quiz | Quiz, Question, QuizAttempt, Certificate | Assessment system |
| AI/RAG | RAGEngine, VectorStore | AI infrastructure |
