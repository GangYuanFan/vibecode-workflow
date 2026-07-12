# 📜 Project AI Rules (`AI_RULES.md`)

The "Constitution" for the AI Agent. Project-specific constraints that override general preferences.

## 🛠️ Coding Standards
- **Language/Framework:** (e.g., TypeScript 5.0+, React 18)
- **Stylistic Constraints:** 
    - [ ] Use Functional Components over Classes.
    - [ ] All API responses must follow the `{ data, error }` envelope.
    - [ ] Use `Zod` for all input validation.
- **Naming Conventions:** (e.g., `kebab-case` for files, `camelCase` for variables)

## 🚫 Forbidden Patterns
- No `any` types in TypeScript.
- No direct DB calls from the Controller; use the Service layer.
- No inline styles; use Tailwind CSS.

## 🧪 Testing Requirements
- Every new function must have at least one "Happy Path" and one "Sad Path" assertion.
- Minimum test coverage for core logic: 80%.

---
*Rule: Defined in Phase 1. Referenced by the Agent in every Phase 3 implementation.*
