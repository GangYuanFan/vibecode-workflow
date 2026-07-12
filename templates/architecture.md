# 🏗️ System Architecture (`ARCHITECTURE.md`)

The living document of the system's structural design. Unlike the Blueprint, this evolves with the project.

## 1. High-Level Design
- **Core Purpose:** (Briefly describe what the system does)
- **Architecture Pattern:** (e.g., Layered, Hexagonal, Event-Driven)
- **Data Flow:** (High-level description of how data moves through the system)

## 2. Component Map
| Component | Responsibility | Technology | Dependencies |
| :--- | :--- | :--- | :--- |
| API Gateway | Routing, Rate Limiting | Express.js | Auth Middleware |
| User Service | Profile Mgmt | Node.js | MongoDB |

## 3. Critical Paths
- **Path A:** (e.g., User Login $\rightarrow$ JWT Generation $\rightarrow$ Session Store)
- **Path B:** (e.g., Profile Update $\rightarrow$ Cache Invalidation $\rightarrow$ DB Write)

## 4. Infrastructure & Deployment
- **Environment:** (e.g., Docker, AWS Lambda)
- **CI/CD:** (e.g., GitHub Actions $\rightarrow$ Vercel)

---
*Rule: This file must be updated whenever a "Decision" in `DECISIONS.md` changes the structural design.*
