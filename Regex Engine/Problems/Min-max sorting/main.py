def minmax_selection_sort(l):
    for i in range(len(l)-1):
        index = i
        for j in range(i+1, len(l)):
            if not i % 2 and l[j] < l[index] \
                    or i % 2 and l[j] > l[index]:
                index = j

        l[index], l[i] = l[i], l[index]


l = [int(d) for d in input().split()]
minmax_selection_sort(l)
print(" ".join([str(elem) for elem in l]))
