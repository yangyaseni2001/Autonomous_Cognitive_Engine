from agents import llm


def composer_qc(output):

    prompt = f"""
Evaluate this report.

Criteria:
1. Structure
2. Completeness
3. Professionalism

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