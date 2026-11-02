from agents import llm


def explorer_qc(output):

    prompt = f"""
You are a Quality Checker.

Evaluate the research output.

Criteria:
1. Relevance
2. Completeness
3. Accuracy

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