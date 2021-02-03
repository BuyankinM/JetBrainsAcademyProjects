def check(x):
    try:
        price = int(x)
        if 120 < price < 137:
            print(price)
        else:
            raise ValueError
    except ValueError:
        print("That's a bad present!")