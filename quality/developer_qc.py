from agents import llm


def developer_qc(output):

    prompt = f"""
Evaluate code quality.

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