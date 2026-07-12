# ⚖️ Technical Decision Log (`DECISIONS.md`)

This file records the "WHY" behind technical choices to prevent "Decision Drift" and "Circular Debugging."

| Date | Component | Decision | Alternatives Considered | Reason for Choice | Impact/Risk |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-07-12 | DB Layer | Use MongoDB over PostgreSQL | SQL, DynamoDB | Schema flexibility for user profile metadata | Eventual consistency on some reads |
| 2026-07-12 | Auth | Use JWT with short expiry | Session Cookies | Server-side sessions | Scalability across multiple API nodes |

---
*Rule: Any choice that departs from the 'Standard Library' or 'Simplest Path' MUST be logged here.*
