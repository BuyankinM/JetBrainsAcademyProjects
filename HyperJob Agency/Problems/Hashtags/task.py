message = input()

tag = ""
start_tag = 0
for c in message:
    if c == "#":
        start_tag += 1
    elif c in " .,!?":
        if start_tag == 1 and tag:
            print(tag)
        start_tag = 0
        tag = ""
    elif start_tag == 1:
        tag += c
else:
    if start_tag == 1 and tag:
        print(tag)
