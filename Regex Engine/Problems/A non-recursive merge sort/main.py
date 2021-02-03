def merge(left, right):
    merged = [0 for _ in range(len(left) + len(right))]
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        merged[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        merged[k] = right[j]
        j += 1
        k += 1

    return merged


num_list = [[int(d)] for d in input().split()]

while len(num_list) > 1:
    temp_l = []
    n, ost = divmod(len(num_list), 2)

    for ii in range(n):
        temp_l.append(merge(num_list[2 * ii], num_list[2 * ii + 1]))

    if ost:
        temp_l.append(num_list[-1])

    num_list = temp_l[:]

print(" ".join([str(d) for d in num_list[0]]))
