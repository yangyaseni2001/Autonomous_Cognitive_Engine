from agents import llm
from tools.todo_tool import create_todo


def planner_agent(state):

    query = state["user_query"]

    prompt = f"""
You are a Planner Agent.

Your job is to break the user request into TODO tasks.

Available Agents:

1. Explorer
   - Research
   - Search
   - Gather information

2. Analysis
   - Compare
   - Evaluate
   - Analyze

3. Developer
   - Coding
   - Technical Design
   - Architecture

4. Composer
   - Documentation
   - Reports
   - Articles

5. General
   - Everything else

Return format:

Task | Agent

User Request:
{query}
"""

    response = llm.invoke(prompt)

    todos = []

    lines = response.content.split("\n")

    for line in lines:

        if "|" in line:

            task, agent = line.split("|")

            todos.append(
                create_todo(
                    task.strip(),
                    agent.strip()
                )
            )

    state["todos"] = todos

    return state