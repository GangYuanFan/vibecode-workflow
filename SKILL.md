---
name: vibecode-workflow
description: "Coding workflow methodology: plan, search, test, verify"
version: 1.0.0
---

# Coding Workflow

A disciplined coding methodology: **plan architecture first → search before build → test incrementally → verify fully**.

---

## When to Use

**Every coding task.** This is the default workflow. Do not start writing code without going through each phase.

---

## The Four Phases

```
Phase 1  ──  Global Route Planning   →  Architecture + Method Map
Phase 2  ──  Ponytail + GitHub Search →  Reuse + Minimal Build
Phase 3  ──  Incremental Testing     →  Partial Unit Verify
Phase 4  ──  Full Verification       →  Complete System Test
```

---

## Phase 1 — Global Route Planning

**Before writing a single line of code**, plan the complete route.

### 1.1 Architecture Overview
- What are the inputs and outputs?
- What components exist? (frontend, backend, database, external APIs)
- Draw the data flow: from user action to result and back.
- Identify all files that will be touched or created.

### 1.2 Method Call Map
- List every function, method, and API endpoint that needs to exist or be modified.
- For each: responsibility, inputs, outputs.
- Identify call chains: which function calls which.

### 1.3 Dependency Check
- What dependencies are already installed?
- What new dependencies would be needed? (Ask before adding.)

### 1.4 Output
A short plan (3–10 lines) describing: files to touch, functions to create or modify, and the test strategy.

---

## Phase 2 — Ponytail + GitHub Search

### 2.1 Search Before Build
Before writing custom code:
1. **Search GitHub** for existing repos, gists, or snippets that solve the same problem.
2. **Check stdlib** — can the language's standard library cover this?
3. **Check installed dependencies** — does something already installed handle this?

### 2.2 Ponytail Ladder
Stop at the first rung that holds:

| Rung | Question |
|------|----------|
| 1 | **Does this need to exist at all?** YAGNI — skip if not strictly needed. |
| 2 | **Stdlib does it?** Use it. |
| 3 | **Platform feature covers it?** CSS over JS, DB constraint over app code. |
| 4 | **Already-installed dependency?** Never add a new dependency for what a few lines can do. |
| 5 | **Can it be one line?** One line. |
| 6 | Only then: the minimum code that works. |

### 2.3 Ponytail Rules
- No unrequested abstractions (no interface with one implementation, no factory for one product).
- No boilerplate "for later" — later can scaffold for itself.
- Deletion over addition. Boring over clever.
- Fewest files possible. Shortest working diff wins.
- Mark deliberate simplifications with `ponytail:` comments noting the ceiling and upgrade path.

---

## Phase 3 — Incremental Testing

**After writing each partial unit of work, test it immediately.**

### 3.1 What Counts as a Partial Unit
- A single function
- A single API endpoint
- A single UI component or view
- A single file modification

### 3.2 Unit Test Checklist
- [ ] Does it run without syntax or compile errors?
- [ ] Does it produce the expected output for normal inputs?
- [ ] Does it handle edge cases? (empty input, null, boundary values)
- [ ] Does it fail gracefully on invalid input?

### 3.3 Test Methods

| Language / Scope | Check | Command |
|-----------------|-------|---------|
| JavaScript | Syntax | `node -e "new Function(code)"` |
| Python | Syntax | `python3 -m py_compile file.py` |
| HTML | JS blocks | Extract `<script>` and run through `new Function()` |
| API endpoint | Live test | `curl -s -w "%{http_code}" <url>` |
| Logic | Inline assert | Small demo script or `assert`-based self-check |

### 3.4 Rule: No "Build Everything Then Test"
- Never write multiple functions without testing the first one.
- If a unit fails, fix it before moving to the next unit.
- Accumulate confidence as you go.

---

## Phase 4 — Full Verification

**After all units are complete, run the full system test.**

### 4.1 Full Test Checklist
- [ ] All syntax checks pass (all files).
- [ ] All API endpoints return expected status codes.
- [ ] Frontend renders without console errors.
- [ ] All user-facing features work end-to-end.
- [ ] No hardcoded paths or credentials left behind.
- [ ] No dead code or unused imports.
- [ ] No regression: existing features still work.

### 4.2 Sign-off
Only after all checks pass, deliver the result to the user. If any check fails, go back to Phase 3 to fix, then re-run Phase 4.

---

## Error Recovery

If a test fails at any phase:
1. **Read the error message carefully** — identify the exact line and error type.
2. **Fix only the failing code** — do not rewrite unrelated parts.
3. **Re-run the test** for that unit.
4. **Continue** to the next unit or re-run Phase 4.

---

## Quick Reference Card

```
```
┌────────────────────────────────────────────────────────┐
│  Coding Workflow                                       │
├────────────────────────────────────────────────────────┤
│                                                        │
│  1. PLAN    ──── 架構規劃 + 方法調用地圖                │
│                   (寫 code 前完成)                      │
│                                                        │
│  2. SEARCH  ──── GitHub 搜尋 + ponytail 最小化          │
│                   (不重複造輪子)                        │
│                                                        │
│  3. IMPLEMENT ── 根據規劃實際寫 code                    │
│                   (寫 code)                             │
│                                                        │
│  4. TEST    ──── 每寫一個功能 → 立刻測試               │
│                   (累積信心，不堆債)                    │
│                                                        │
│  5. VERIFY  ──── 全部完成 → 全面驗證                   │
│                   (沒有遺漏才交貨)                      │
│                                                        │
└────────────────────────────────────────────────────────┘
```
```

## Changelog

### 1.0.0 (2026-07-11)
- Initial release
- Four-phase workflow: Plan → Search → Test → Verify
- Ponytail integration with GitHub-first search
- Incremental and full verification checklists
