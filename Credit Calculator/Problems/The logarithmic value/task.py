import math
a, base = int(input()), int(input())
if base > 1:
    print(round(math.log(a, base), 2))
else:
    print(round(math.log(a), 2))