for n in range(1, 101):
    res = ""

    if not n % 3:
        res += "Fizz"

    if not n % 5:
        res += "Buzz"

    if not res:
        res = str(n)

    print(res)