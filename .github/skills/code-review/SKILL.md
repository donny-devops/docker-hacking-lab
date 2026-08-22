---
name: code-review
description: Guidelines for conducting code reviews on pull requests.
---

# Code Review Skill

## Overview
Perform thorough, constructive code reviews focusing on security, code quality, testing, and standard architecture practices.

## Guidelines

### 1. Security & Authentication
- Verify that endpoints requiring authentication use appropriate guards/middleware.
- Ensure sensitive configurations load via environment variables rather than hardcoded strings.
- Validate incoming payload schemas to prevent injection vulnerabilities.

### 2. Code Quality & Architecture
- Ensure type annotations are fully defined across function signatures.
- Keep controller/handler logic thin by delegating business logic to service layers.
- Check for redundant logic or missed modularization opportunities.

### 3. Testing
- Confirm new features or bug fixes include corresponding unit or integration tests.
- Verify test suites pass without regressions.

## Review Output Format
Structure review feedback as follows:
- **Summary**: Concise high-level overview.
- **Critical/Blocking**: Security risks, bugs, or breaking changes.
- **Suggestions**: Non-blocking improvements or refactoring advice.
- **Positives**: Notable well-implemented design decisions.
