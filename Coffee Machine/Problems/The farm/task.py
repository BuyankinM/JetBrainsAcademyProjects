Chicken: 23
Goat: 678
Pig: 1296
Cow: 3848
Sheep: 6769

money = int(input())
if money >= 23:
    if money >= 6769:
        n = money // 6769
        word = "sheep"
    elif money >= 3848:
        n = money // 3848
        word = "cow"
    elif money >= 1296:
        n = money // 1296
        word = "pig"
    elif money >= 678:
        n = money // 678
        word = "goat"
    else:
        n = money // 23
        word = "chicken"

    if n > 1 and word != "sheep":
        word += "s"

    print(f"{n} {word}")

else:

    print("None")
