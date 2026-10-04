def goal_driven_agent(temp):
    goal = 72

    if temp > goal:
        return "COOL"
    elif temp < goal:
        return "HEAT"
    else:
        return "IDLE"

temperature = 85

while temperature != 72:
    action = goal_driven_agent(temperature)
    print(f"Temperature: {temperature} -> Action: {action}")

    if action == "COOL":
        temperature -= 1
    elif action == "HEAT":
        temperature += 1

print(f"Temperature: {temperature} -> Goal reached!")
