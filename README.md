# Agentic AI Research Assistant

## Overview
This project implements a planner-driven agentic AI system capable of autonomously performing academic research tasks, including knowledge retrieval, synthesis, experimentation planning, self-reflection, and IEEE-style PDF generation.

Unlike traditional LLM-based systems, the proposed framework decomposes intelligence into specialized agents coordinated by a central planner, enabling autonomous reasoning and real-world tool execution.

## System Architecture
The system consists of the following agents:
- Planner Agent (task decomposition and routing)
- Retrieval Agent (vector-based knowledge retrieval)
- Memory Agent (context persistence)
- Research Agent (outline construction)
- Experiment Agent (hypothesis and experiment generation)
- Synthesis Agent (academic writing)
- Tool Agent (PDF generation and web tools)
- Reflection Agent (evaluation and logging)

## Key Features
- End-to-end autonomous research workflow
- Planner-driven multi-agent architecture
- IEEE-style research paper generation in PDF format
- Safety-aware synthesis with fallback handling
- Modular and extensible design

## Installation

```bash
git clone https://github.com/<your-username>/agentic-ai-research-assistant.git
cd agentic-ai-research-assistant
pip install -r requirements.txt
