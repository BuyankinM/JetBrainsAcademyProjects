def count_selection_sort(l):
    n = 0
    for i in range(len(l)-1):
        min_ind = i
        for j in range(i+1, len(l)):
            if l[j] < l[min_ind]:
                min_ind = j
                n += 1

        if min_ind != i:
            l[min_ind], l[i] = l[i], l[min_ind]

    return n


lists = []
for _ in range(int(input())):
    lists.append([int(d) for d in input().split()])

ind, num = 0, 0
for i, l in enumerate(lists):
    nl = count_selection_sort(l)
    if nl > num:
        ind, num = i, nl

print(ind, num)
