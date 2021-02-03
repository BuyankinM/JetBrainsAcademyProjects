s = 0
sq = 0
while True:
    d = int(input())
    s += d
    sq += d * d
    if not s:
        break
print(sq)
