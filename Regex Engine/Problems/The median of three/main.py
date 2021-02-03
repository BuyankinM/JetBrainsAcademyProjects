def choose_median(lst, start, middle, end):
    if len(lst) < 3:
        return 0
    elif lst[start] <= lst[middle] <= lst[end] \
            or lst[end] <= lst[middle] <= lst[start]:
        return middle
    elif lst[middle] <= lst[start] <= lst[end] \
            or lst[end] <= lst[start] <= lst[middle]:
        return start
    else:
        return end


def partition(lst, start, end):
    j = start

    for i in range(start + 1, end + 1):
        if lst[i] <= lst[start]:
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]
    return j


data = list(map(int, input().split()))
copy_data = data[:]

mid_ind = len(data) // 2 - (1 if not len(data) % 2 else 0)
med = choose_median(data, 0, mid_ind, len(data) - 1)
partition(data, med, 0, len(data) - 1)

print(med)

rr = " ".join([str(d) for d in data])
print(" ".join([str(d) for d in data]))

