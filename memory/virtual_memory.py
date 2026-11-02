def write_file(state, filename, content):
    """
    Save content into virtual memory.
    """

    state["virtual_files"][filename] = content


def read_file(state, filename):
    """
    Read content from virtual memory.
    """

    return state["virtual_files"].get(
        filename,
        "File Not Found"
    )


def edit_file(state, filename, new_content):
    """
    Update file content.
    """

    if filename in state["virtual_files"]:
        state["virtual_files"][filename] = new_content


def ls(state):
    """
    List all virtual files.
    """

    return list(state["virtual_files"].keys())