# from agents import llm


# def composer_agent(state):

#     todo = state["current_todo"]

#     prompt = f"""
#     Create a professional report.

#     Task:
#     {todo['task']}
#     """

#     response = llm.invoke(prompt)

#     state["outputs"][todo["id"]] = response.content

#     return state


# from agents import llm
# from quality.composer_qc import composer_qc


# def composer_agent(state):

#     todo = state["current_todo"]

#     retries = 2

#     for attempt in range(retries):

#         prompt = f"""
# Create a professional report.

# Task:
# {todo['task']}
# """

#         response = llm.invoke(prompt)

#         output = response.content

#         score = composer_qc(output)

#         print(
#             f"Composer QC Score: {score}"
#         )

#         if score >= 80:

#             state["outputs"][todo["id"]] = output

#             return state

#     state["outputs"][todo["id"]] = output

#     return state





from agents import llm
from quality.composer_qc import composer_qc
from memory.virtual_memory import write_file


def composer_agent(state):

    todo = state["current_todo"]

    retries = 2

    for attempt in range(retries):

        prompt = f"""
        Create a professional report.

        Task:
        {todo['task']}
        """

        response = llm.invoke(prompt)

        output = response.content

        score = composer_qc(output)

        print(f"Composer QC Score: {score}")

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