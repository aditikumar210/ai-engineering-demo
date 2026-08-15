# AI Software Engineering Assistant

A multi-agent AI system that analyzes GitHub issues and coordinates requirements analysis, coding analysis, code review, testing, bug investigation, and documentation through specialised AI agents.

## 1. Problem Analysis

### 1.1 Business Context

Software development teams spend significant time manually analyzing GitHub issues, understanding requirements, planning implementations, reviewing code, designing tests, investigating bugs, and documenting changes. This project automates and coordinates these activities using specialised AI agents while keeping a human approval step before repository changes.

### 1.2 Stakeholders

- Software developers
- Software engineering teams
- Code reviewers
- QA/testing engineers
- Project/engineering managers
- Repository maintainers

### 1.3 Problem Statement

Traditional software engineering workflows require multiple manual handoffs between requirements analysis, implementation planning, code review, testing, debugging, and documentation. This can lead to delays, inconsistent outputs, and missed information. The proposed system uses multiple specialised AI agents that collaborate through structured handoffs and shared workflow context to streamline this process.

### 1.4 Objectives

- Automate GitHub issue analysis.
- Use specialised AI agents for different software-engineering tasks.
- Enable structured agent-to-agent handoffs.
- Maintain shared workflow context using `WorkflowState`.
- Generate structured outputs using Pydantic models.
- Include testing and bug-investigation stages.
- Generate implementation documentation.
- Include human approval before repository changes.
- Provide error handling throughout the workflow.
- Demonstrate a complete end-to-end multi-agent engineering workflow.
