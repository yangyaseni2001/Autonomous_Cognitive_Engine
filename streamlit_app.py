# import streamlit as st
# from graph.workflow import graph

# st.set_page_config(
#     page_title="Autonomous Cognitive Engine",
#     layout="wide"
# )

# st.title("🧠 Autonomous Cognitive Engine")
# st.subheader("Deep Research & Long Horizon Task Agent")

# query = st.chat_input("Enter your task...")

# if query:

#     st.chat_message("user").write(query)

#     with st.spinner("Running Agents..."):

#         state = {
#             "user_query": query,
#             "todos": [],
#             "current_todo": {},
#             "completed_tasks": [],
#             "outputs": {},
#             "virtual_files": {},
#             "combined_output": "",
#             "final_output": ""
#         }

#         result = graph.invoke(state)

#     st.chat_message("assistant").write(
#         result["final_output"]
#     )




import streamlit as st

from agents.planner_agent import planner_agent
from tools.task_router import task_router
from agents.combiner_agent import combiner_agent
from quality.final_qc import final_qc


st.set_page_config(
    page_title="Autonomous Cognitive Engine",
    layout="wide"
)

# st.title("🧠 Autonomous Cognitive Engine")
st.title(" Autonomous Cognitive Engine")
st.subheader("Deep Research & Long Horizon Tasks")

query = st.text_area(
    "Enter your task:",
    height=120
)

if st.button("Run Agent"):

    state = {
        "user_query": query,
        "todos": [],
        "current_todo": {},
        "completed_tasks": [],
        "outputs": {},
        "virtual_files": {},
        "combined_output": "",
        "final_output": ""
    }

    # Planner
    state = planner_agent(state)

    st.header("Generated TODOs")

    for todo in state["todos"]:
        st.write(todo)

    # Execute TODOs
    for todo in state["todos"]:

        state["current_todo"] = todo

        state = task_router(state)

    # Combine
    state = combiner_agent(state)

    # Final QC
    score = final_qc(
        state["combined_output"]
    )

    st.header("Final QC Score")

    st.success(score)

    state["final_output"] = state["combined_output"]

    st.header("Final Output")

    st.write(
        state["final_output"]
    )
    