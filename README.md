# 🤖 Workflow Orchestrator: AI-Driven Workflow Orchestrator

> **"Monitor Bitcoin price, and if it drops 5%, send me an SMS and buy via Binance API."**
>
> Stop coding your automations. Start speaking them.

---

## 💡 Project Overview

**Workflow Orchestrator** is a final year project that transforms natural language goals into executable, multi-step workflows. Leveraging the power of Large Language Models (LLMs) and LangChain's agentic capabilities, this system acts as a "AI Programmer" for popular workflow automation platforms like n8n or Zapier.

Our goal is to eliminate the need for manual, technical configuration of automations. Users simply state what they want to achieve, and AutoFlow autonomously plans, generates, and executes the complete workflow.

### Key Technology Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Backend API** | **FastAPI** (Python) | High-performance API server for handling requests. |
| **Frontend UI** | **Next.js** (React) | Modern, responsive user interface for interaction. |
| **LLM Reasoning** | **SLM (Small/Specialized LLM)** | The "brain" for planning and generating workflow JSON. |
| **Agentic Framework** | **LangChain** | Connects the LLM to custom tools for workflow construction. |
| **Data & Logging** | **PostgreSQL** | Database for user authentication and logging of prompts/outputs. |
| **Containerization** | **Docker & Docker Compose** | Ensures a consistent, reliable local development environment. |

---

## ✨ Features

* **Natural Language to Workflow:** Input any goal (e.g., "Post my new blog to Twitter and LinkedIn") and receive a complete, ready-to-execute workflow definition.
* **Human-in-the-Loop:** A dedicated UI feature that allows users to review and manually correct the generated workflow JSON before execution, ensuring safety and precision.
* **Robust Agent Planning:** Utilizes a **RAG (Retrieval-Augmented Generation)** system to provide the LLM with up-to-date documentation and context about the connected workflow platform's APIs.
* **Workflow Execution:** Dedicated backend endpoint (`/execute-workflow`) to securely trigger the created automation on the target platform.
* **Workflow History:** Track all generated and executed workflows via a dedicated user dashboard.

---

The project is structured into four focused phases.

### Phase 1: Local Setup & Core MVP (Weeks 1-4)
**Goal:** Get the entire application stack running reliably on every team member's computer using Docker. Prove the core **prompt-to-JSON** flow works locally.

### Phase 2: Feature Integration & Data Logging (Weeks 5-8)
**Goal:** Build out all core features, including **authentication** and **data logging** (for the prompt and corrected JSON), within the local Docker environment.

### Phase 3: AI Specialization & Finalization (Weeks 9-12)
**Goal:** Fine-tune the **SLM** (Small Language Model) with logged data and finalize all application features, ensuring the project is stable and ready for a final demonstration.

### Phase 4: Documentation & Deployment Planning (Post-Week 12)
**Goal:** Create the final project deliverables, including the report, presentation, and a detailed **Deployment Guide** for future public launch on platforms like Render or Vercel.

### Team Responsibilities

| Role | Core Focus |
| :--- | :--- |
| **Lead Dev (Backend)** | FastAPI, database connection, `/generate-workflow` and `/execute-workflow` endpoints. |
| **AI Specialist (RAG & LLM)** | V1 RAG system, SLM fine-tuning, performance evaluation, and LangChain integration. |
| **Frontend Dev (UI/UX)** | Next.js UI, login/signup pages, "Human-in-the-Loop" editor, and workflow history. |
| **DevOps & QA Engineer** | Docker setup, PostgreSQL service, **automated integration testing** (pytest), and end-to-end quality assurance. |

---

## 🤝 Contribution & Support

This project is the culmination of our final year efforts. For questions, bug reports, or feature requests, please reach out to the team members listed in the project documentation.
