import uuid


def create_todo(task, agent):

    return {
        "id": f"TODO-{str(uuid.uuid4())[:8]}",
        "task": task,
        "agent": agent,
        "status": "pending"
    }