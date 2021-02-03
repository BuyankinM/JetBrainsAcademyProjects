l_win = []
for _ in range(int(input())):
    name, res = input().split()
    if res == "win":
        l_win.append(name)
print(l_win)
print(len(l_win))