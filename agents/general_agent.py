from agents import llm


def general_agent(state):

    todo = state["current_todo"]

    response = llm.invoke(todo["task"])

    state["outputs"][todo["id"]] = response.content

    return state