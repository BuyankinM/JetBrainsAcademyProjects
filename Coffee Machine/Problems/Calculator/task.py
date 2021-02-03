a, b, oper = float(input()), float(input()), input()

if oper == "+":
    print(f"{a + b}")
elif oper == "-":
    print(f"{a - b}")
elif oper == "*":
    print(f"{a * b}")
elif oper == "/":
    print(f"{a / b}" if b != 0 else "Division by 0!")
elif oper == "mod":
    print(f"{a % b}" if b != 0 else "Division by 0!")
elif oper == "pow":
    print(f"{a ** b}")
elif oper == "div":
    print(f"{a // b}" if b != 0 else "Division by 0!")
