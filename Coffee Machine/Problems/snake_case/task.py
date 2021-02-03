s = input()
l = []
for c in s:
    if c == c.upper():
        l.append("_")
        l.append(c.lower())
    else:
        l.append(c)

print("".join(l))