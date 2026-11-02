from agents import llm


def general_qc(output):

    prompt = f"""
Evaluate output quality.

Return ONLY score.

Output:
{output}
"""

    response = llm.invoke(prompt)

    try:
        score = int(response.content.strip())
    except:
        score = 50

    return score