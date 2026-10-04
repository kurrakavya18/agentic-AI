def run(max_iters=10):
    state = {
        "done": False,
        "steps": 0,
    }

    for _ in range(max_iters):
        state["steps"] += 1

        # Your logic here
        success = False

        if success:
            state["done"] = True
            return state

    return {
        **state,
        "result": "failure",
    }
