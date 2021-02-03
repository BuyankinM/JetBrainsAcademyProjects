def solve():
    hidden_operand = "IT'S NOT"
    oper = "not"

    if hidden_operation("ORRR") == "ORRR":
        oper = "or"
        hidden_operand = hidden_operation(False)
    elif hidden_operation("") == "":
        oper = "and"
        hidden_operand = hidden_operation(1)

    print(oper)
    if hidden_operand != "IT'S NOT":
        print(hidden_operand)
