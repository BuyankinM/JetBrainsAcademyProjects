max_cats = 0
name_cats = ""
while True:
    s = input()
    if s == "MEOW":
        break
    name, num = s.split(" ")
    num = int(num)
    if num > max_cats:
        name_cats = name
        max_cats = num
print(name_cats)