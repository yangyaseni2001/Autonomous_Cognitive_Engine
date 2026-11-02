# # # from typing import TypedDict, List, Dict


# # # class AgentState(TypedDict):

# # #     user_query: str

# # #     todos: List[dict]

# # #     current_todo: dict

# # #     completed_tasks: List[str]

# # #     outputs: Dict[str, str]

# # #     final_output: str




# # from typing import TypedDict, List, Dict


# # class AgentState(TypedDict):

# #     user_query: str

# #     todos: List[dict]

# #     current_todo: dict

# #     completed_tasks: List[str]

# #     outputs: Dict[str, str]

# #     virtual_files: Dict[str, str]

# #     combined_output: str

# #     final_output: str






# from typing import TypedDict, List, Dict


# class AgentState(TypedDict):

#     user_query: str

#     todos: List[dict]

#     current_todo: dict

#     completed_tasks: List[str]

#     outputs: Dict[str, str]

#     virtual_files: Dict[str, str]

#     combined_output: str

#     final_output: str


# ------

from typing import TypedDict, List, Dict


class AgentState(TypedDict):

    user_query: str

    todos: List[dict]

    current_todo: dict

    completed_tasks: List[str]

    outputs: Dict[str, str]

    virtual_files: Dict[str, str]

    combined_output: str

    final_output: str