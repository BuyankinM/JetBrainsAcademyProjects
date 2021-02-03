def what_to_do(instructions: str):
    if instructions.startswith("Simon says"):
        return f"I {instructions[11:]}"
    elif instructions.endswith("Simon says"):
        return f"I {instructions[:-11]}"
    return "I won't do it!"
