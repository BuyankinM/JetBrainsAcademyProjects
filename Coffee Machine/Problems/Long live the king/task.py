x, y = int(input()), int(input())
if 2 <= x <= 7 and 2 <= y <= 7:
    print(8)
elif (x in (1, 8) and 2 <= y <= 7) or (y in (1, 8) and 2 <= x <= 7):
    print(5)
else:
    print(3)