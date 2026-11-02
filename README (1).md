# Autonomous Cognitive Engine (ACE) for Deep Research

A Python-based, stateful multi-agent research platform that turns a user
request into a structured research report. The application uses
LangGraph to orchestrate specialized agents, LangChain and Groq for
LLM-powered tasks, and a virtual memory layer to retain intermediate
outputs during execution.

## Overview

Traditional chat interfaces generally respond to a prompt in a single
interaction. The **Autonomous Cognitive Engine (ACE)** follows a
structured workflow:

1.  Understands the user's research task.
2.  Breaks the task into smaller TODO items.
3.  Routes work to specialized agents.
4.  Stores intermediate results in virtual memory.
5.  Evaluates generated content through quality checks.
6.  Combines validated results into a final report.

The project includes a terminal-based entry point and a Streamlit
interface.

## Key Features

-   **Task planning:** Converts a broad request into actionable TODO
    items.
-   **Multi-agent workflow:** Separates planning, exploration, analysis,
    composition, and quality evaluation.
-   **Agent orchestration:** Uses LangGraph to coordinate the stateful
    workflow.
-   **Virtual memory:** Saves and retrieves intermediate task outputs.
-   **Quality control:** Evaluates generated content before it is
    included in the final response.
-   **Research report generation:** Produces a consolidated report from
    the completed workflow.
-   **Two ways to run:** Use the terminal application or the Streamlit
    web interface.

## Technology Stack

  -----------------------------------------------------------------------
  Area                                Technologies
  ----------------------------------- -----------------------------------
  Language                            Python 3.11+

  Workflow orchestration              LangGraph

  LLM application framework           LangChain

  Model provider                      Groq

  Model configured in project         `llama-3.3-70b-versatile`
  documentation                       

  User interface                      Streamlit

  Configuration                       python-dotenv

  Validation and typing               Pydantic, typing-extensions

  Optional tracing                    LangSmith
  -----------------------------------------------------------------------

## Architecture

``` text
User Request
    |
    v
Planner Agent
    |
    v
TODO Generation
    |
    v
Explorer Agent
    |
    v
Analysis Agent
    |
    v
Virtual Memory
    |
    v
Composer Agent
    |
    v
Quality Control (QC) Agent
    |
    v
Final Research Report
    |
    v
Terminal / Streamlit Interface
```

### Agent responsibilities

  -----------------------------------------------------------------------
  Component                           Responsibility
  ----------------------------------- -----------------------------------
  Planner Agent                       Understands the request and creates
                                      structured tasks.

  Explorer Agent                      Gathers information needed for the
                                      assigned task.

  Analysis Agent                      Processes and organizes the
                                      gathered information.

  Composer Agent                      Combines validated results into a
                                      readable report.

  QC Agent                            Evaluates output quality and
                                      supports validation.

  Virtual Memory                      Stores and retrieves intermediate
                                      task outputs.

  LangGraph workflow                  Coordinates the execution flow and
                                      shared state.
  -----------------------------------------------------------------------

## Project Structure

``` text
Autonomous_Cognitive_Engine/
├── agents/
│   ├── __init__.py
│   ├── planner_agent.py
│   ├── explorer_agent.py
│   ├── analysis_agent.py
│   ├── composer_agent.py
│   └── qc_agent.py
├── graph/
│   └── workflow.py
├── memory/
│   └── virtual_memory.py
├── quality/
├── tools/
├── app.py
├── streamlit_app.py
├── requirements.txt
├── .gitignore
└── README.md
```

The `quality/` and `tools/` folders contain supporting project modules.
The exact files may vary as the project evolves.

## Getting Started

### 1. Prerequisites

-   Python 3.11 or later
-   Git
-   A Groq API key
-   A terminal or code editor such as Visual Studio Code

### 2. Clone the repository

``` bash
git clone https://github.com/yangyaseni2001/Autonomous_Cognitive_Engine.git
cd Autonomous_Cognitive_Engine
```

### 3. Create and activate a virtual environment

**Windows PowerShell**

``` powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use Command Prompt:

``` bat
.venv\Scripts\activate.bat
```

**macOS / Linux**

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### 4. Install dependencies

``` bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Configure environment variables

Create a file named `.env` in the project root. Add your own API key
values:

``` env
GROQ_API_KEY=your_groq_api_key

# Optional: only needed if LangSmith tracing is enabled in your setup
LANGCHAIN_API_KEY=your_langsmith_api_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=Autonomous_Cognitive_Engine
```

Replace the placeholder values with your own credentials. **Never commit
`.env` or publish API keys.** The repository's `.gitignore` should
exclude `.env`.

If you do not use LangSmith, leave its optional variables unset unless
your local configuration requires them.

## Run the Application

### Option A: Terminal application

From the project root, with the virtual environment activated:

``` bash
python app.py
```

Follow the prompt in the terminal and enter the research task you want
the engine to process.

### Option B: Streamlit web application

``` bash
streamlit run streamlit_app.py
```

Then open the local address displayed in the terminal. By default,
Streamlit uses:

``` text
http://localhost:8501
```

Enter a research request in the interface and start execution.

## Example Research Request

``` text
Research the applications of Generative AI in healthcare and prepare a structured report.
```

The workflow can plan the task, delegate work to the relevant agents,
retain intermediate outputs, evaluate the results, and compose a final
report.

## Example Workflow Output

The project's documentation illustrates a workflow with agent routing
and quality scores, for example:

``` text
Routing to: Explorer
Explorer QC Score: 85

Routing to: Composer
Composer QC Score: 95

Final QC Score: 95
```

These are illustrative values, not a guarantee that every run will
produce the same scores or output.

## Configuration and Security

-   Keep API keys in `.env`, not directly in Python source files.
-   Do not commit `.env`, access tokens, passwords, or private
    credentials.
-   If a credential was accidentally pushed to a remote repository,
    revoke or rotate it with the provider.
-   Keep `.env.example` limited to placeholder values if you want to
    document required environment variables.
-   Avoid committing virtual environments, cache files, and local editor
    settings.

## Current Scope

ACE demonstrates task decomposition, multi-agent coordination, virtual
memory, quality evaluation, and automated report composition. Its output
depends on the configured LLM, prompts, available tools, and the quality
of the task input.

## Potential Future Enhancements

-   Web-search integration with source-aware research.
-   PDF and other export formats for generated reports.
-   Persistent database-backed memory.
-   More advanced agent collaboration and task routing.
-   Agent execution and quality analytics.
-   User authentication and multi-user support.
-   Cloud deployment and production monitoring.

## Author

**Yangyaseni Sahoo**

Developed as part of the **Infosys PMIS Internship Program**.

## Repository

[Autonomous Cognitive Engine on
GitHub](https://github.com/yangyaseni2001/Autonomous_Cognitive_Engine)

------------------------------------------------------------------------

If you encounter an installation or execution issue, check that the
virtual environment is active, dependencies are installed, and the
required environment variables are configured.
