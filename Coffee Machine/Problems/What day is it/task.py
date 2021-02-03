offset = int(input())

if offset > 13:
    print("Wednesday")
elif -10 <= offset <= 13:
    print("Tuesday")
else:
    print("Monday")