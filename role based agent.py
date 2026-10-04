def agent_role(temp):
    if temp > 100:
        return "COOL"
    else:
        return "IDLE"

temperature = 105
role = agent_role(temperature)

print(f"Temperature: {temperature}")
print(f"Agent role: {role}")
