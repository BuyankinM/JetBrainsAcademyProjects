while True:
    s = int(input())

    if s < 10:
        continue

    if s > 100:
        break
    else:
        print(s)