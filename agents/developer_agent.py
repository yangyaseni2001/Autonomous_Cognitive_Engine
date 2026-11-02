from agents import llm


def developer_agent(state):

    todo = state["current_todo"]

    prompt = f"""
    Complete this development task:

    {todo['task']}
    """

    response = llm.invoke(prompt)

    state["outputs"][todo["id"]] = response.content

    return state