import numpy as np


l = []
for _ in range(3):
    l.append(int(input()))

a = np.array(l)
print(a.std())