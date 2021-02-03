scores = input().split()
n = 0
m = 0
for s in scores:
    if s == "C":
        n += 1
    else:
        m += 1

    if m == 3:
        print("Game over")
        break
else:
    print("You won")

print(n)