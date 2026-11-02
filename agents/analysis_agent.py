from agents import llm


def analysis_agent(state):

    todo = state["current_todo"]

    prompt = f"""
    Analyze:

    {todo['task']}
    """

    response = llm.invoke(prompt)

    state["outputs"][todo["id"]] = response.content

    return state