from agents import llm
from memory.virtual_memory import read_file


def combiner_agent(state):

    all_content = []

    # Read every virtual file
    for filename in state["virtual_files"]:

        content = read_file(
            state,
            filename
        )

        all_content.append(content)

    combined_text = "\n\n".join(all_content)

    prompt = f"""
You are a Combiner Agent.

Tasks:

1. Combine all information.
2. Remove duplicate content.
3. Remove repeated paragraphs.
4. Keep unique information only.
5. Create one clean consolidated document.

Content:

{combined_text}
"""

    response = llm.invoke(prompt)

    state["combined_output"] = response.content

    return state