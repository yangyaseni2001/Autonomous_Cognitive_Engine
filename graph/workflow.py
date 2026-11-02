from langgraph.graph import StateGraph, END

from graph.state import AgentState

from agents.planner_agent import planner_agent
from tools.task_router import task_router
from agents.combiner_agent import combiner_agent
from agents.final_agent import final_agent


def planner_node(state):

    return planner_agent(state)


def execute_todos_node(state):

    for todo in state["todos"]:

        state["current_todo"] = todo

        state = task_router(state)

    return state


def combiner_node(state):

    return combiner_agent(state)


def final_node(state):

    return final_agent(state)


workflow = StateGraph(AgentState)

workflow.add_node(
    "planner",
    planner_node
)

workflow.add_node(
    "execute_todos",
    execute_todos_node
)

workflow.add_node(
    "combiner",
    combiner_node
)

workflow.add_node(
    "final",
    final_node
)

workflow.set_entry_point(
    "planner"
)

workflow.add_edge(
    "planner",
    "execute_todos"
)

workflow.add_edge(
    "execute_todos",
    "combiner"
)

workflow.add_edge(
    "combiner",
    "final"
)

workflow.add_edge(
    "final",
    END
)

graph = workflow.compile()