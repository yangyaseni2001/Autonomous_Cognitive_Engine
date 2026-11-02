# # # from agents.planner_agent import planner_agent

# # # state = {
# # #     "user_query": "Research Artificial Intelligence and create a report",
# # #     "todos": [],
# # #     "current_todo": {},
# # #     "completed_tasks": [],
# # #     "outputs": {},
# # #     "final_output": ""
# # # }

# # # result = planner_agent(state)

# # # print("\nGenerated TODOs:\n")

# # # for todo in result["todos"]:

# # #     print(todo)

# # # from agents.planner_agent import planner_agent
# # # from tools.task_router import task_router


# # # def main():

# # #     query = input("\nEnter Task: ")

# # #     state = {
# # #         "user_query": query,
# # #         "todos": [],
# # #         "current_todo": {},
# # #         "completed_tasks": [],
# # #         "outputs": {},
# # #         "virtual_files": {},
# # #         "combined_output": "",
# # #         "final_output": ""
# # #     }

# # #     # Planner
# # #     state = planner_agent(state)

# # #     print("\nGenerated TODOs:\n")

# # #     for todo in state["todos"]:

# # #         print(todo)

# # #     # Execute TODOs

# # #     for todo in state["todos"]:

# # #         state["current_todo"] = todo

# # #         state = task_router(state)

# # #     print("\n\nAGENT OUTPUTS\n")

# # #     for todo_id, output in state["outputs"].items():

# # #         print("=" * 80)

# # #         print(todo_id)

# # #         print(output[:500])

# # #         print()


# # # if __name__ == "__main__":
# # #     main()













# # from agents.planner_agent import planner_agent
# # from tools.task_router import task_router
# # from memory.virtual_memory import read_file


# # def main():

# #     query = input("\nEnter Task: ")

# #     state = {
# #         "user_query": query,
# #         "todos": [],
# #         "current_todo": {},
# #         "completed_tasks": [],
# #         "outputs": {},
# #         "virtual_files": {},
# #         "combined_output": "",
# #         "final_output": ""
# #     }

# #     # Planner Agent
# #     state = planner_agent(state)

# #     print("\nGenerated TODOs:\n")

# #     for todo in state["todos"]:
# #         print(todo)

# #     # Execute TODOs
# #     for todo in state["todos"]:

# #         state["current_todo"] = todo

# #         state = task_router(state)

# #     # Display Agent Outputs
# #     print("\n\nAGENT OUTPUTS\n")

# #     for todo_id, output in state["outputs"].items():

# #         print("=" * 80)

# #         print(todo_id)

# #         print(output[:500])

# #         print()

# #     # Display Virtual Memory Files
# #     print("\n")
# #     print("=" * 80)
# #     print("VIRTUAL MEMORY FILES")
# #     print("=" * 80)

# #     for file in state["virtual_files"]:
# #         print(file)

# #     # Display Virtual Memory Contents
# #     print("\n")
# #     print("=" * 80)
# #     print("FILE CONTENTS")
# #     print("=" * 80)

# #     for file, content in state["virtual_files"].items():

# #         print(f"\n{file}")

# #         print("-" * 40)

# #         print(content[:300])

# #     # Test read_file()
# #     print("\n")
# #     print("=" * 80)
# #     print("READ FILE TEST")
# #     print("=" * 80)

# #     if state["virtual_files"]:

# #         first_file = list(
# #             state["virtual_files"].keys()
# #         )[0]

# #         content = read_file(
# #             state,
# #             first_file
# #         )

# #         print(f"\nReading: {first_file}\n")

# #         print(content[:500])


# # if __name__ == "__main__":
# #     main()












# from agents.planner_agent import planner_agent
# from agents.combiner_agent import combiner_agent
# from tools.task_router import task_router
# from memory.virtual_memory import read_file


# def main():

#     query = input("\nEnter Task: ")

#     state = {
#         "user_query": query,
#         "todos": [],
#         "current_todo": {},
#         "completed_tasks": [],
#         "outputs": {},
#         "virtual_files": {},
#         "combined_output": "",
#         "final_output": ""
#     }

#     # Planner Agent
#     state = planner_agent(state)

#     print("\nGenerated TODOs:\n")

#     for todo in state["todos"]:
#         print(todo)

#     # Execute TODOs
#     for todo in state["todos"]:

#         state["current_todo"] = todo

#         state = task_router(state)

#     # Run Combiner Agent
#     state = combiner_agent(state)

#     # Display Agent Outputs
#     print("\n\nAGENT OUTPUTS\n")

#     for todo_id, output in state["outputs"].items():

#         print("=" * 80)

#         print(todo_id)

#         print(output[:500])

#         print()

#     # Display Virtual Memory Files
#     print("\n")
#     print("=" * 80)
#     print("VIRTUAL MEMORY FILES")
#     print("=" * 80)

#     for file in state["virtual_files"]:
#         print(file)

#     # Display Virtual Memory Contents
#     print("\n")
#     print("=" * 80)
#     print("FILE CONTENTS")
#     print("=" * 80)

#     for file, content in state["virtual_files"].items():

#         print(f"\n{file}")

#         print("-" * 40)

#         print(content[:300])

#     # Combined Output
#     print("\n")
#     print("=" * 80)
#     print("COMBINED OUTPUT")
#     print("=" * 80)

#     print(state["combined_output"][:1500])

#     # Test read_file()
#     print("\n")
#     print("=" * 80)
#     print("READ FILE TEST")
#     print("=" * 80)

#     if state["virtual_files"]:

#         first_file = list(
#             state["virtual_files"].keys()
#         )[0]

#         content = read_file(
#             state,
#             first_file
#         )

#         print(f"\nReading: {first_file}\n")

#         print(content[:500])


# if __name__ == "__main__":
#     main()




# ----------------------------------------------------------------------------------
# from agents.planner_agent import planner_agent
# from agents.combiner_agent import combiner_agent
# from agents.final_agent import final_agent
# from tools.task_router import task_router
# from memory.virtual_memory import read_file


# def main():

#     query = input("\nEnter Task: ")

#     state = {
#         "user_query": query,
#         "todos": [],
#         "current_todo": {},
#         "completed_tasks": [],
#         "outputs": {},
#         "virtual_files": {},
#         "combined_output": "",
#         "final_output": ""
#     }

#     # ==========================
#     # Planner Agent
#     # ==========================

#     state = planner_agent(state)

#     print("\nGenerated TODOs:\n")

#     for todo in state["todos"]:
#         print(todo)

#     # ==========================
#     # Execute TODOs
#     # ==========================

#     for todo in state["todos"]:

#         state["current_todo"] = todo

#         state = task_router(state)

#     # ==========================
#     # Combiner Agent
#     # ==========================

#     state = combiner_agent(state)

#     # ==========================
#     # Final QC Agent
#     # ==========================

#     state = final_agent(state)

#     # ==========================
#     # Agent Outputs
#     # ==========================

#     print("\n\nAGENT OUTPUTS\n")

#     for todo_id, output in state["outputs"].items():

#         print("=" * 80)

#         print(todo_id)

#         print(output[:500])

#         print()

#     # ==========================
#     # Virtual Memory Files
#     # ==========================

#     print("\n")
#     print("=" * 80)
#     print("VIRTUAL MEMORY FILES")
#     print("=" * 80)

#     for file in state["virtual_files"]:
#         print(file)

#     # ==========================
#     # File Contents
#     # ==========================

#     print("\n")
#     print("=" * 80)
#     print("FILE CONTENTS")
#     print("=" * 80)

#     for file, content in state["virtual_files"].items():

#         print(f"\n{file}")

#         print("-" * 40)

#         print(content[:300])

#     # ==========================
#     # Combined Output
#     # ==========================

#     print("\n")
#     print("=" * 80)
#     print("COMBINED OUTPUT")
#     print("=" * 80)

#     print(state["combined_output"][:1500])

#     # ==========================
#     # Final Output
#     # ==========================

#     print("\n")
#     print("=" * 80)
#     print("FINAL OUTPUT")
#     print("=" * 80)

#     print(state["final_output"][:2000])

#     # ==========================
#     # Read File Test
#     # ==========================

#     print("\n")
#     print("=" * 80)
#     print("READ FILE TEST")
#     print("=" * 80)

#     if state["virtual_files"]:

#         first_file = list(
#             state["virtual_files"].keys()
#         )[0]

#         content = read_file(
#             state,
#             first_file
#         )

#         print(f"\nReading: {first_file}\n")

#         print(content[:500])


# if __name__ == "__main__":
#     main()


# ----------------------------------------
from graph.workflow import graph


def main():

    query = input(
        "\nEnter Task: "
    )

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

    result = graph.invoke(state)

    print("\n")
    print("=" * 80)
    print("FINAL OUTPUT")
    print("=" * 80)

    print(
        result["final_output"][:30000]
    )


if __name__ == "__main__":
    main()