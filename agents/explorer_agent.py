# from agents import llm


# def explorer_agent(state):

#     todo = state["current_todo"]

#     prompt = f"""
#     Research in detail:

#     {todo['task']}
#     """

#     response = llm.invoke(prompt)

#     state["outputs"][todo["id"]] = response.content

#     return state


# from agents import llm
# from quality.explorer_qc import explorer_qc


# def explorer_agent(state):

#     todo = state["current_todo"]

#     retries = 2

#     for attempt in range(retries):

#         prompt = f"""
# Research:

# {todo['task']}
# """

#         response = llm.invoke(prompt)

#         output = response.content

#         score = explorer_qc(output)

#         print(
#             f"Explorer QC Score: {score}"
#         )

#         if score >= 80:

#             state["outputs"][todo["id"]] = output

#             return state

#     state["outputs"][todo["id"]] = output

#     return state


from agents import llm
from quality.explorer_qc import explorer_qc
from memory.virtual_memory import write_file


def explorer_agent(state):

    todo = state["current_todo"]

    retries = 2

    for attempt in range(retries):

        prompt = f"""
        Research the following topic in detail:

        {todo['task']}
        """

        response = llm.invoke(prompt)

        output = response.content

        score = explorer_qc(output)

        print(f"Explorer QC Score: {score}")

        if score >= 80:

            # Store in outputs
            state["outputs"][todo["id"]] = output

            # Store in virtual memory
            filename = f"{todo['id']}.txt"

            write_file(
                state,
                filename,
                output
            )

            return state

    # Fallback if QC never reaches 80
    state["outputs"][todo["id"]] = output

    filename = f"{todo['id']}.txt"

    write_file(
        state,
        filename,
        output
    )

    return state