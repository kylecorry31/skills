---
name: ci-failure
description: Use when given a failing CI run or job, or asked why CI failed.
argument-hint: "<run or job URL> [investigate only | fix]"
---

Investigate the failing CI run or job to identify what caused it to fail. Implement a fix if possible, or provide a detailed explanation of why no fix is needed. Do not push, re-run, or cancel workflows; ask the user to perform those actions if necessary.