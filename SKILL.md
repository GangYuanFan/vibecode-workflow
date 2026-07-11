---
name: vibecode-workflow
description: "Coding workflow methodology: plan, search, test, verify"
version: 1.0.3
---

# Coding Workflow

A disciplined coding methodology: **plan architecture first → search before
build → implement & test in iterative loop → verify fully**.

---

## When to Use

**Every coding task.** This is the default workflow. Do not start writing code
without going through each phase.

---

## The Five Phases (Iterative)

```
Phase 1  ──  Global Route Planning     →  Architecture + Method Map
Phase 2  ──  Ponytail + GitHub Search   →  Reuse + Minimal Build

Phase 3  ──  Implementation (one module at a time)
Phase 4  ──  Incremental Testing (test that module)
     ↑                    │
     ╰──── ← pass ──────╯
          ← fail → fix → retest

Phase 5  ──  Full Verification           →  Complete System Test
```

Phase 3 and Phase 4 form an **iterative loop**:

1. Implement ONE module/block (Phase 3)
2. Test it immediately (Phase 4)
   - PASS → go back to step 1 for the next module
   - FAIL → fix, retest, then back to step 1 for next module
3. Repeat until ALL modules are done
4. Proceed to Phase 5 (Full Verification)

---

## Phase 1 — Global Route Planning

**Before writing a single line of code**, plan the complete route.

### 1.1 Architecture Overview
- What are the inputs and outputs?
- What components exist? (frontend, backend, database, external APIs)
- Draw the data flow: from user action to result and back.
- Identify all files that will be touched or created.

### 1.2 Method Call Map
- List every function, method, and API endpoint that needs to exist or be
  modified.
- For each: responsibility, inputs, outputs.
- Identify call chains: which function calls which.

### 1.3 Dependency Check
- What dependencies are already installed?
- What new dependencies would be needed? (Ask before adding.)

### 1.4 Output
A short plan (3–10 lines) describing: files to touch, functions to create or
modify, and the test strategy.

---

## Phase 2 — Ponytail + GitHub Search

### 2.1 Search Before Build
Before writing custom code:
1. **Search GitHub** for existing repos, gists, or snippets that solve the
   same problem.
2. **Check stdlib** — can the language's standard library cover this?
3. **Check installed dependencies** — does something already installed handle
   this?

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
- No unrequested abstractions (no interface with one implementation, no factory
  for one product).
- No boilerplate "for later" — later can scaffold for itself.
- Deletion over addition. Boring over clever.
- Fewest files possible. Shortest working diff wins.
- Mark deliberate simplifications with `ponytail:` comments noting the ceiling
  and upgrade path.

---

## Phase 3 & 4 — Iterative Implement & Test Loop

Phases 3 and 4 work together as a loop. Do NOT implement everything first and
test later.

### The Loop

```
         ┌─────────────────────────────┐
         │  Phase 3: Implement one     │
         │  module / block             │
         └──────────┬──────────────────┘
                    │
                    ▼
         ┌─────────────────────────────┐
         │  Phase 4: Test that module  │
         └──────────┬──────────────────┘
                    │
             ┌──────┴──────┐
             │             │
            PASS          FAIL
             │             │
             │        Fix code
             │             │
             └──────┬──────┘
                    │
             ┌──────┴──────┐
             │             │
        more modules?  All done
             │             │
             ▼             ▼
     back to Phase 3   Phase 5
```

### Phase 3 — Implementation

#### 3.1 Follow the Plan
- Write code according to Phase 1's architecture and method map.
- Start with the smallest, most independent unit first.
- Keep functions focused — one responsibility per function.
- **Implement only ONE module/block at a time.**

#### 3.2 Code Style
- Use the ponytail ladder from Phase 2 to keep it minimal.
- Avoid premature optimization. Make it work, then make it right.
- Add comments for non-obvious logic and `ponytail:` simplifications.

### Phase 4 — Incremental Testing

**After writing ONE unit, test it immediately. Do not write a second unit
before testing the first.**

#### 4.1 What Counts as a Unit
- A single function
- A single API endpoint
- A single UI component or view
- A single file modification

#### 4.2 Unit Test Checklist
- [ ] Does it run without syntax or compile errors?
- [ ] Does it produce the expected output for normal inputs?
- [ ] Does it handle edge cases? (empty input, null, boundary values)
- [ ] Does it fail gracefully on invalid input?

#### 4.3 Test Methods

| Language / Scope | Check | Command |
|-----------------|-------|---------|
| JavaScript | Syntax | `node -e "new Function(code)"` |
| Python | Syntax | `python3 -m py_compile file.py` |
| HTML | JS blocks | Extract `<script>` and run through `new Function()` |
| API endpoint | Live test | `curl -s -w "%{http_code}" <url>` |
| Logic | Inline assert | Small demo script or `assert`-based self-check |

#### 4.4 Decision: Pass or Fail?
- **PASS** → Go back to Phase 3 to implement the next module/block.
- **FAIL** → Fix the code, re-run Phase 4 test, repeat until it passes.
- Never skip to the next module when the current one is failing.

---

## Phase 5 — Full Verification

**Only enter Phase 5 when ALL modules are implemented and individually tested.**
This is a mandatory gate — do not deliver without passing this phase.

### 5.1 Full Test Checklist
- [ ] All syntax checks pass (all files).
- [ ] All API endpoints return expected status codes.
- [ ] Frontend renders without console errors.
- [ ] All user-facing features work end-to-end.
- [ ] No hardcoded paths or credentials left behind.
- [ ] No dead code or unused imports.
- [ ] No regression: existing features still work.
- [ ] *(Self-reference)* This skill itself was followed: verify before
  publishing.

### 5.2 Sign-off
Only after all checks pass, deliver the result to the user. If any check fails,
go back to Phase 4 to fix, then re-run Phase 5.

### 5.3 Self-Correction
If the user points out a mistake that Phase 5 should have caught:
1. Fix the bug immediately.
2. Add the missed check to the Phase 5 checklist so it's never missed again.
3. Log the failure to prevent recurrence.

---

## Error Recovery

If a test fails at any phase:
1. **Read the error message carefully** — identify the exact line and error
   type.
2. **Fix only the failing code** — do not rewrite unrelated parts.
3. **Re-run the test** for that unit.
4. If in Phase 3/4 loop: retest, then continue to next module.
5. If in Phase 5: go back to Phase 4, fix, then re-run Phase 5.

---

## Quick Reference Card

```
┌───────────────────────────────────────────────────────────┐
│  Coding Workflow                                          │
├───────────────────────────────────────────────────────────┤
│                                                           │
│  1. PLAN     ──── 架構規劃 + 方法調用地圖                  │
│                    (寫 code 前完成)                        │
│                                                           │
│  2. SEARCH   ──── GitHub 搜尋 + ponytail 最小化            │
│                    (不重複造輪子)                          │
│                                                           │
│  3. IMPLEMENT ─ 實作一個 module/block                      │
│                    (做一個)                                │
│        │                                                  │
│  4. TEST    ──── 局部測試 ←── pass ── 回 Phase 3          │
│        │                   (下一塊)                       │
│     fail ── 修正 → retest                                 │
│        │                                                  │
│     全部做完 ──→ Phase 5                                  │
│                                                           │
│  5. VERIFY   ──── 全局驗證 (全部完成才做)                  │
│                    (沒有遺漏才交貨)                        │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

---

## Changelog

### 1.0.3 (2026-07-11)
- Fixed all ASCII art alignment (box drawing characters)
- Simplified loop diagram for readability
- Changed overview diagram to text-based loop description

### 1.0.2 (2026-07-11)
- Fixed workflow to be iterative: Phase 3 ↔ Phase 4 loop
- Updated diagrams to show the loop

### 1.0.1 (2026-07-11)
- Added missing Phase 3 (Implementation)
- Fixed Quick Reference Card alignment
- Added Self-Correction section to Phase 5
- Phase 5 checklist now includes self-reference check

### 1.0.0 (2026-07-11)
- Initial release
- Five-phase workflow: Plan → Search → Implement → Test → Verify
- Ponytail integration with GitHub-first search
- Incremental and full verification checklists
