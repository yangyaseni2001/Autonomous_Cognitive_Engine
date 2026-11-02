from agents import llm
from quality.final_qc import final_qc


def final_agent(state):

    combined_output = state["combined_output"]

    retries = 2

    for attempt in range(retries):

        score = final_qc(combined_output)

        print(
            f"Final QC Score: {score}"
        )

        if score >= 70:

            state["final_output"] = combined_output

            return state

        prompt = f"""
Improve the following document.

Make it:

- More complete
- Better structured
- More professional

Document:

{combined_output}
"""

        response = llm.invoke(prompt)

        combined_output = response.content

    state["final_output"] = combined_output

    return state