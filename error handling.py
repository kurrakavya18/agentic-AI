def run(max_iters=10):
    state = {
        "done": False,
        "steps": 0,
        "status": None,
        "log": [],
    }

    while not state["done"] and state["steps"] < max_iters:
        state["steps"] += 1

        action = get_action()

        # Handle invalid action
        if action not in {"success", "continue"}:
            error = {
                "error": "invalid_action",
                "message": f"Invalid action: {action}",
                "step": state["steps"],
            }

            state["status"] = "failure"
            state["log"].append(error)
            return state

        state["log"].append({
            "step": state["steps"],
            "action": action,
        })

        if action == "success":
            state["done"] = True
            state["status"] = "success"
            return state

    state["status"] = "failure"
    state["log"].append({
        "step": state["steps"],
        "error": "max_iters_exceeded",
    })

    return state
