# Autonomous Cognitive Engine (ACE) for Deep Research

## Project Overview

The Autonomous Cognitive Engine (ACE) is a Streamlit-based multi-agent research platform developed using Python, LangGraph, LangChain, and Groq LLM. The system is designed to automate research workflows by breaking complex tasks into manageable subtasks, routing them to specialized agents, storing intermediate outputs in memory, validating results, and generating a final structured report.

Unlike traditional AI chatbots, ACE follows a stateful workflow that enables planning, memory management, quality evaluation, and autonomous execution.

---

# Project Objectives

* Automate research and report generation.
* Decompose complex tasks into structured TODO items.
* Route tasks to specialized agents.
* Store intermediate outputs using virtual memory.
* Validate generated content through quality checks.
* Provide a user-friendly Streamlit interface.
* Demonstrate LangGraph-based stateful workflow orchestration.

---

# Technology Stack

## Programming Language

* Python 3.11+

## Frameworks & Libraries

* LangGraph
* LangChain
* LangChain-Groq
* Python-Dotenv
* Streamlit

## AI Model

* Groq LLM
* Model: llama-3.3-70b-versatile

## Development Tools

* Visual Studio Code
* Git
* LangSmith (Optional Monitoring & Tracing)

---

# Project Structure

```text
autonomous_cognitive_engine/

│
├── agents/
│   ├── __init__.py
│   ├── planner_agent.py
│   ├── explorer_agent.py
│   ├── analysis_agent.py
│   ├── composer_agent.py
│   └── qc_agent.py
│
├── graph/
│   └── workflow.py
│
├── memory/
│   └── virtual_memory.py
│
├── streamlit_app.py
├── app.py
├── .env
├── requirements.txt
└── README.txt
```

---

# System Workflow

## Step 1: User Task Submission

The user enters a research request through the Streamlit interface.

### Example

```text
Research Artificial Intelligence and create a report
```

---

## Step 2: Task Planning

The Planner Agent analyzes the request and generates structured TODO items.

### Example

```text
TODO 1: Research Artificial Intelligence

TODO 2: Create a report on Artificial Intelligence
```

---

## Step 3: Agent Routing

The workflow routes tasks to appropriate agents.

### Agents Used

* Planner Agent
* Explorer Agent
* Analysis Agent
* Composer Agent
* QC Agent

---

## Step 4: Research & Analysis

The Explorer Agent gathers information and the Analysis Agent processes the collected content.

---

## Step 5: Virtual Memory Storage

Intermediate outputs are stored in the Virtual File System (VFS).

### Example Files

```text
TODO-123.txt

TODO-456.txt
```

The system can later retrieve these files when generating the final report.

---

## Step 6: Quality Evaluation

Generated outputs are evaluated using quality scores.

### Example

```text
Explorer QC Score: 85

Composer QC Score: 95

Final QC Score: 95
```

Only validated outputs proceed to the next stage.

---

## Step 7: Final Report Generation

The Composer Agent consolidates all validated outputs into a structured research report.

---

# Workflow Architecture

```text
User (Streamlit UI)

        ↓

Planner Agent

        ↓

Explorer Agent

        ↓

Analysis Agent

        ↓

Virtual Memory System

        ↓

Composer Agent

        ↓

QC Agent

        ↓

Final Research Report

        ↓

Displayed in Streamlit UI
```

---

# Core Features

## Intelligent Task Planning

* Automatic TODO generation.
* Structured execution workflow.
* Task decomposition before processing.

## Multi-Agent Architecture

* Specialized agents for different responsibilities.
* Modular workflow execution.
* Better task organization.

## Virtual Memory System

* Stores intermediate outputs.
* Reduces context overload.
* Enables information retrieval during execution.

## Quality Control Mechanism

* Evaluates generated content.
* Ensures output consistency.
* Improves reliability of final reports.

## Interactive Streamlit Interface

* User-friendly web application.
* Easy task submission.
* Real-time result display.
* Professional project demonstration interface.

---

# Environment Setup

## Create Virtual Environment

```bash
python -m venv .venv
```

---

## Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a file named `.env`

```env
GROQ_API_KEY=your_groq_api_key

LANGCHAIN_API_KEY=your_langsmith_api_key

LANGCHAIN_TRACING_V2=true

LANGCHAIN_PROJECT=Autonomous_Cognitive_Engine
```

---

# Running the Application

## Launch Streamlit Application

Activate the virtual environment:

```bash
.venv\Scripts\activate
```

Run:

```bash
streamlit run streamlit_app.py
```

---

## Open in Browser

```text
http://localhost:8501
```

---

# User Workflow

### Step 1

Open the Streamlit application.

### Step 2

Enter a research topic.

Example:

```text
Research Python Programming
```

### Step 3

Click the Execute button.

### Step 4

Planner Agent generates TODO items.

### Step 5

Research Agents process the task.

### Step 6

Quality checks validate outputs.

### Step 7

Final report is generated and displayed on the Streamlit interface.

---

# Sample Execution

### User Input

```text
Research Python Programming
```

### Execution

```text
Routing to: Explorer

Explorer QC Score: 85

Routing to: Composer

Composer QC Score: 95

Final QC Score: 95
```

---

# Output

The system generates a structured research report containing:

* Introduction
* Key Concepts
* Applications
* Analysis
* Conclusion

---

# Virtual Memory System

The Virtual File System (VFS) stores intermediate outputs during execution.

### Operations

* Write File
* Read File
* Update Content
* Retrieve Research Notes

### Benefits

* Persistent context storage.
* Reduced token consumption.
* Efficient retrieval of intermediate results.

---

# Quality Assurance

The project incorporates evaluation mechanisms to improve output quality.

### Evaluation Metrics

* Task Completion
* Output Consistency
* Agent Performance
* Report Structure
* Quality Control Scores

---

# Future Enhancements

* Real-Time Web Search Integration
* PDF Report Generation
* Database-Based Persistent Storage
* Advanced Multi-Agent Collaboration
* Agent Performance Analytics Dashboard
* User Authentication System
* Cloud Deployment
* Real-Time Monitoring with LangSmith

---

# Project Outcome

The Autonomous Cognitive Engine successfully demonstrates:

✔ Intelligent Task Planning

✔ Multi-Agent Collaboration

✔ Virtual Memory Management

✔ Quality Evaluation

✔ Research Automation

✔ Streamlit-Based User Interface

✔ LangGraph Stateful Workflow Execution

---

# Conclusion

The Autonomous Cognitive Engine (ACE) is a Streamlit-based multi-agent research platform that combines task planning, virtual memory, quality evaluation, and autonomous execution into a unified workflow. By leveraging LangGraph, LangChain, and Groq LLM, the system transforms user research requests into structured and validated reports through an intelligent and scalable architecture.

---

## Developed Under

**Infosys PMIS Internship Program**

**Project Title:** Autonomous Cognitive Engine (ACE) for Deep Research

**Developer:** Yangyaseni Sahoo
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Autonomous Cognitive Engine (ACE) for Deep Research

## Project Overview

The Autonomous Cognitive Engine (ACE) is a stateful multi-agent research system developed using Python, LangGraph, LangChain, and Groq LLM. The platform is designed to automate complex research workflows by decomposing user tasks into manageable subtasks, assigning them to specialized agents, validating outputs, and generating a final consolidated report.

Unlike traditional AI chatbots, ACE follows a structured workflow that includes task planning, agent routing, quality evaluation, and virtual memory management.

---

## Objectives

* Automate research and report generation.
* Break complex tasks into structured TODO items.
* Route tasks to specialized agents.
* Maintain intermediate outputs using virtual memory.
* Improve output quality through evaluation and validation.
* Demonstrate stateful AI workflow orchestration.

---

## Technology Stack

### Programming Language

* Python 3.11+

### Frameworks & Libraries

* LangGraph
* LangChain
* LangChain-Groq
* Python-Dotenv
* Streamlit

### AI Model

* Groq LLM
* Model: llama-3.3-70b-versatile

### Development Tools

* Visual Studio Code
* Git
* LangSmith (Optional Monitoring)

---

## Project Structure

autonomous_cognitive_engine/

├── agents/

│ ├── **init**.py

│ ├── planner_agent.py

│ ├── explorer_agent.py

│ ├── analysis_agent.py

│ ├── composer_agent.py

│ └── qc_agent.py

│

├── graph/

│ └── workflow.py

│

├── memory/

│ └── virtual_memory.py

│

├── streamlit_app.py

├── app.py

├── .env

├── requirements.txt

└── README.txt

---

## Workflow Architecture

### Step 1: User Task Submission

The user provides a research request.

Example:

Research Artificial Intelligence and create a report

---

### Step 2: Task Planning

The Planner Agent analyzes the request and generates TODO items.

Example:

* Research Artificial Intelligence
* Create a report on Artificial Intelligence

---

### Step 3: Agent Routing

Tasks are assigned to appropriate agents.

Examples:

Explorer Agent → Information Gathering

Analysis Agent → Content Analysis

Composer Agent → Report Creation

QC Agent → Quality Validation

---

### Step 4: Virtual Memory Storage

Intermediate outputs are stored in the Virtual File System (VFS).

Example:

TODO-123.txt

TODO-456.txt

The system can later read these files during report generation.

---

### Step 5: Quality Evaluation

Generated outputs are evaluated.

Example:

Explorer QC Score: 85

Composer QC Score: 95

Final QC Score: 95

Only validated outputs proceed to the next stage.

---

### Step 6: Final Report Generation

The Composer Agent consolidates all validated outputs into a final research document.

---

## Features

### Intelligent Task Planning

* Automatic TODO generation.
* Structured workflow execution.

### Multi-Agent Architecture

* Specialized agents for different responsibilities.
* Improved task organization.

### Virtual Memory System

* Stores intermediate research outputs.
* Reduces context overload.

### Quality Control

* Evaluates generated content.
* Ensures better output consistency.

### Streamlit User Interface

* Interactive web-based interface.
* Easy task submission and output visualization.

---

## Environment Setup

### Create Virtual Environment

Windows:

python -m venv .venv

Activate Environment:

.venv\Scripts\activate

---

### Install Dependencies

pip install -r requirements.txt

---

## Environment Variables

Create a .env file:

GROQ_API_KEY=your_groq_api_key

LANGCHAIN_API_KEY=your_langsmith_api_key

LANGCHAIN_TRACING_V2=true

LANGCHAIN_PROJECT=Autonomous_Cognitive_Engine

---

## Running the Application

### Terminal Version

python app.py

Example:

Enter Task: Research Artificial Intelligence and create a report

---

### Streamlit Version

streamlit run streamlit_app.py

Open:

http://localhost:8501

---

## Sample Execution Flow

User Request

↓

Planner Agent

↓

TODO Generation

↓

Explorer Agent

↓

Analysis Agent

↓

Composer Agent

↓

QC Evaluation

↓

Virtual Memory Storage

↓

Final Consolidated Report

---

## Output Example

Routing to: Explorer

Explorer QC Score: 85

Routing to: Composer

Composer QC Score: 95

Final QC Score: 95

The system then generates a structured research report based on the user request.

---

## Future Enhancements

* Real-time Web Search Integration
* Advanced Agent Collaboration
* Database-Based Persistent Memory
* PDF Report Generation
* Multi-User Support
* Agent Performance Analytics
* Dashboard-Based Monitoring

---

## Conclusion

The Autonomous Cognitive Engine demonstrates how stateful workflows, task planning, virtual memory, and multi-agent collaboration can be combined to create an intelligent research automation platform. The project successfully transforms a simple user query into a structured, validated, and comprehensive research report through autonomous execution.

---

Developed as part of the Infosys PMIS Internship Program.
