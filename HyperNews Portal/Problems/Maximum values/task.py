import numpy as np

vals = []

while True:
    try:
        val = int(input())
        vals.append(val)
    except EOFError:
        break

arr = np.array(vals)
print(f"""{arr.max()}
{arr.argmax()}""")
