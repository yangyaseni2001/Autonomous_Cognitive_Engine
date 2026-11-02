from agents import llm


def final_qc(output):

    prompt = f"""
You are a Final Quality Checker.

Evaluate the document based on:

1. Completeness
2. Accuracy
3. Structure
4. Relevance
5. Professional Quality

Return ONLY a number between 0 and 100.

Document:

{output}
"""

    response = llm.invoke(prompt)

    try:
        score = int(response.content.strip())
    except:
        score = 50

    return score