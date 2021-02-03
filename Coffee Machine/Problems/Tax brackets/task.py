income = int(input())
if income <= 15_527:
    tax_percent = 0
elif 15_528 <= income <= 42_707:
    tax_percent = 15
elif 42_708 <= income <= 132_406:
    tax_percent = 25
else:
    tax_percent = 28

print(f"The tax for {income} is {tax_percent}%. That is {round(income * tax_percent / 100)} dollars!")
