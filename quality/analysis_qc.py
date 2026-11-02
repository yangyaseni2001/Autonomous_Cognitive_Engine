from agents import llm


def analysis_qc(output):

    prompt = f"""
Evaluate this analysis.

Return ONLY a score from 0 to 100.

Output:
{output}
"""

    response = llm.invoke(prompt)

    try:
        score = int(response.content.strip())
    except:
        score = 50

    return score