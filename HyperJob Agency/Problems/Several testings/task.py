def check(x: str):
    if x.isdigit():
        val = int(x)
        if val >= 202:
            print(val)
        else:
            print("There are less than 202 apples! You cheated on me!")
    else:
        print("It is not a digit!")