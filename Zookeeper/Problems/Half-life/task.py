N, R = int(input()), int(input())

s = 0
while N > R:
    N /= 2
    s += 12

print(s)