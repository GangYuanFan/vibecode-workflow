---
name: vibecode-workflow
description: "Enterprise coding workflow: Plan $\rightarrow$ Search $\rightarrow$ Implement $\rightarrow$ Test $\rightarrow$ Verify with full Audit Trail"
version: 2.2.0
---

<!--
# AGENT ENFORCEMENT GUARDRAIL
# MANDATORY BEHAVIOR RULES:
# 1. Every response MUST start with a status tag: [CURRENT_PHASE: X]
# 2. STRICTLY PROHIBITED from advancing to Phase N+1 until the user explicitly approves the output of Phase N.
# 3. ZERO-CODE LOCK: In Phase 1 and Phase 2, the Agent's output window MUST contain 0 lines of implementation code.
# 4. MICRO-COMMIT RULE: Only ONE unit per response. After implementing, STOP and output Phase 4 command.
# 5. TOOL-USE ENFORCEMENT: Phase 2 MUST execute at least one search query and print the log.
# 6. AUDIT TRAIL PERSISTENCE: 
#    - Phase 1: Must initialize ARCHITECTURE.md and AI_RULES.md.
#    - Phase 2: Must log technical choices in DECISIONS.md.
#    - Phase 3/4: Must update PROGRESS.md after every successful unit test.
# 7. DEBT LOGGING: Every ponytail shortcut MUST be logged in DEBT.md.
# -------------------------------------------------------------------------------------------
-->

# Coding Workflow v2.2.0 (The Audit Trail Edition)

A disciplined coding methodology designed for high-complexity projects, ensuring that **decisions are logged**, **progress is persisted**, and **architecture is living**.

---

## 0. Agent State Machine (Mandatory)

To prevent skipping phases and ensure "muscle memory" internalization:

1.  **Status Tagging**: Every single response MUST begin with: `[CURRENT_PHASE: X]`.
2.  **Phase Gating**: No advancement to Phase N+1 without explicit user approval.
3.  **Zero-Code Lock**: Absolute prohibition of implementation code in Phase 1 & 2.

---

## The Five Phases (Iterative)

```
Phase 0  ──  Agent State Machine (Status Tagging & Gating)
Phase 1  ──  Planning & Foundation (Architecture, Rules, P5 Plan)
Phase 2  ──  Minimalist Discovery & Decisions (Search + Decision Log)

Phase 3  ──  Implementation (One unit at a time)
Phase 4  ──  Incremental Testing (Assert + Progress Log)
     ↑                    │
     ╰──── ← pass ──────╯
          ← fail → fix → retest

Phase 5  ──  Full Verification & Final Audit (Sign-off + Debt)
```

---

## Phase 1 — Planning & Foundation

**Establish the project's "Constitution" and "Map" before coding.**

### 1.1 Architecture & Rules Initialization
- **Create `AI_RULES.md`**: Define the project-specific coding standards, forbidden patterns, and testing requirements.
- **Create `ARCHITECTURE.md`**: Define the high-level design, component map, and critical data paths.
- **Impact Analysis**: Identify regressions in shared components.

### 1.2 Method Call Map
- Map every function, input, output, and call chain.

### 1.3 Context & Dependency Control
- **Context Pruning**: Define the absolute *minimum* set of files required for the task. Explicitly list files that must be ignored or dropped from the context window to prevent attention dilution and token bloat.

### 1.4 Output: [Phase 1.4 Sign-off Blueprint]
Use `templates/blueprint.md`. **Must include the Phase 5 Comprehensive Verification Plan.**

---

## Phase 2 — Minimalist Discovery & Decisions

### 2.1 Search Verification
- Execute search tools (grep, GitHub, etc.) and print the log.

### 2.2 Decision Logging (`DECISIONS.md`)
- Whenever a technical choice is made (e.g., selecting a library, choosing a data structure), it **MUST** be logged in `DECISIONS.md`.
- Record: Decision $\rightarrow$ Alternatives $\rightarrow$ Reason $\rightarrow$ Risk.

### 2.3 Ponytail Ladder
- Stop at the first rung: YAGNI $\rightarrow$ Stdlib $\rightarrow$ Platform $\rightarrow$ Dependency $\rightarrow$ One-liner $\rightarrow$ Min-code.

---

## Phase 3 & 4 — Iterative Implement & Test Loop

### The Micro-Commit Rule
Implement only ONE unit per response $\rightarrow$ STOP $\rightarrow$ Output Phase 4 command.

### Phase 3 — Implementation
- Follow `ARCHITECTURE.md` and `AI_RULES.md`.
- Mark simplifications with `ponytail:` comments.

### Phase 4 — Incremental Testing & Progress Tracking
- **Logic Assertion**: Verify expected output (Use `templates/assertion.md`).
- **Progress Persistence**: Upon a **PASS**, immediately update `PROGRESS.md` with the unit status and test date. This ensures the Agent can resume after a context wipe.

---

## Phase 5 — Full Verification & Final Audit

### 5.1 Final Verification
- Run the comprehensive plan defined in Phase 1.
- Verify against `AI_RULES.md` (Coding standard audit).

### 5.2 Sign-off & Debt Audit
- **Debt Ledger**: Ensure all `ponytail:` comments are logged in `DEBT.md`.
- **Audit Trail Check**: Ensure `ARCHITECTURE.md`, `DECISIONS.md`, and `PROGRESS.md` are complete.
- **Commit Hygiene**: Atomic, single-purpose commits.

---

## Error Recovery

- **Circuit Breaker**: 3 consecutive failures on one unit $\rightarrow$ Rollback $\rightarrow$ Return to Phase 1.

---

## Quick Reference Card

```
┌───────────────────────────────────────────────────────────┐
│  Coding Workflow v2.2.0                                   │
├───────────────────────────────────────────────────────────┤
│                                                           │
│  0. STATE      ──── [CURRENT_PHASE: X] Tagging            │
│                                                           │
│  1. PLAN       ──── Arch + Rules + Blueprint + P5 Plan     │
│                                                           │
│  2. SEARCH     ──── Search + Decision Log (DECISIONS.md)   │
│                                                           │
│  3. IMPLEMENT  ─ 1 Unit → STOP → Phase 4 Command          │
│                                                           │
│  4. TEST       ──── Logic Assertion + Progress Log         │
│                                                           │
│  5. VERIFY     ──── Full Audit + Debt Ledger              │
└───────────────────────────────────────────────────────────┘
```
