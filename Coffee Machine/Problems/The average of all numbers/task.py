a, b = int(input()), int(input())
s = 0
k = 0
for n in range(a, b + 1):
    if not n % 3:
        s += n
        k += 1

print(s / k)
