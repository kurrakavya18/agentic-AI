def run(max_iters=10):
    state = {
        "done": False,
        "steps": 0,
        "status": None,
    }

    while not state["done"] and state["steps"] < max_iters:
        state["steps"] += 1

        # Your logic here
        success = some_condition()

        if success:
            state["done"] = True
            state["status"] = "success"
            return state

    # Max iterations exceeded
    state["status"] = "failure"
    return state
