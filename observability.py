def run(max_iters=10):
    state = {
        "done": False,
        "steps": 0,
        "status": None,
        "log": [],
    }

    while not state["done"] and state["steps"] < max_iters:
        state["steps"] += 1

        # Log each step
        state["log"].append({
            "step": state["steps"],
            "status": "running",
        })

        # Your logic here
        success = some_condition()

        if success:
            state["done"] = True
            state["status"] = "success"
            state["log"][-1]["status"] = "success"
            return state

    state["status"] = "failure"
    state["log"].append({
        "step": state["steps"],
        "status": "failure",
        "reason": "max_iters exceeded",
    })

    return state
