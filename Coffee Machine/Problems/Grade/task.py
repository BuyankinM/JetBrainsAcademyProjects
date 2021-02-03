score, max_score = int(input()), int(input())
percent = score / max_score * 100

if percent < 60:
    print("F")
elif 60 <= percent < 70:
    print("D")
elif 70 <= percent < 80:
    print("C")
elif 80 <= percent < 90:
    print("B")
else:
    print("A")