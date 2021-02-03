import numpy as np

num_list = []
for _ in range(4):
    num_list.append(int(input()))

a = np.array([num_list[:2], num_list[2:]])
print(a.T)
