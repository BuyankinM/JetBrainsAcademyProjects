def check():
    try:
        x = int(input())
        if 25 <= x <= 37:
            print(x)
        else:
            raise ValueError
    except ValueError:
        print("Correct the error!")