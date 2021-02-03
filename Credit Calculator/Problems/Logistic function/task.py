import math
x = int(input())
log_func = math.exp(x) / (math.exp(x) + 1)
print(round(log_func, 2))