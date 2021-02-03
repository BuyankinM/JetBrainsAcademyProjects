values = []
while True:
    s = input()
    if s == ".":
        break
    values.append(int(s))
print(sum(values) / len(values))