from agents.explorer_agent import explorer_agent
from agents.analysis_agent import analysis_agent
from agents.developer_agent import developer_agent
from agents.composer_agent import composer_agent
from agents.general_agent import general_agent


def task_router(state):

    agent = state["current_todo"]["agent"]

    print(f"\nRouting to: {agent}")

    if agent == "Explorer":
        return explorer_agent(state)

    elif agent == "Analysis":
        return analysis_agent(state)

    elif agent == "Developer":
        return developer_agent(state)

    elif agent == "Composer":
        return composer_agent(state)

    else:
        return general_agent(state)