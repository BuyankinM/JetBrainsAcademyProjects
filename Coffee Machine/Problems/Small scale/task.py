values = []
while True:
    s = input()
    if s == ".":
        break
    values.append(float(s))
print(min(values))