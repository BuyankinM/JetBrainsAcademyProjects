def partition(lst, start, end):

    pivot = lst[start]
    m1 = start
    m2 = start

    for i in range(start + 1, end + 1):
        if lst[i] < pivot:
            lst[i], lst[m1] = lst[m1], lst[i]
            lst[i], lst[m2 + 1] = lst[m2 + 1], lst[i]
            m1 += 1
            m2 += 1
        elif lst[i] == pivot:
            lst[i], lst[m2 + 1] = lst[m2 + 1], lst[i]
            m2 += 1

    return m1, m2


data = list(map(int, input().split()))
j, k = partition(data, 0, len(data) - 1)

print(j, k)
print(" ".join([str(d) for d in data]))
