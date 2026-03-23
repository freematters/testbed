# Implementation Plan: Add hello module

## Checklist
- [x] Step 1: Implement the feature
- [x] Step 2: E2E test

---

## Step 1: Implement the feature

**Depends on**: none

**Objective**: Implement all components described in design.md.

**Sub-items**:
- Create `src/testbed/hello.py` with `hello(name: str) -> str` function returning `f"Hello, {name}!"`
- Create `tests/test_hello.py` with pytest tests: basic greeting, empty string input, importability

**Related Files**: `src/testbed/hello.py`, `tests/test_hello.py`

**Test Requirements**: Run `pytest tests/test_hello.py` — all integration test cases from design.md section 3 must pass.

---

## Step 2: E2E test

**Depends on**: Step 1

**Objective**: Not applicable — e2e tests were excluded in requirements. This step is a no-op.
