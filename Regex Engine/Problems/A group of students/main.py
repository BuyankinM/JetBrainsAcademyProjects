def choose_median(lst, start, middle, end):
    global ind_sort
    
    if len(lst) < 3:
        return 0
    elif lst[start][ind_sort] <= lst[middle][ind_sort] <= lst[end][ind_sort] \
            or lst[end][ind_sort] <= lst[middle][ind_sort] <= lst[start][ind_sort]:
        return middle
    elif lst[middle][ind_sort] <= lst[start][ind_sort] <= lst[end][ind_sort] \
            or lst[end][ind_sort] <= lst[start][ind_sort] <= lst[middle][ind_sort]:
        return start
    else:
        return end


def partition(lst, pivot, start, end):
    global ind_sort

    if ind_sort == 1:
        lst[start], lst[pivot] = lst[pivot], lst[start]

    j = start

    for i in range(start + 1, end + 1):
        if ((ind_sort == 1 or ind_sort == 0 and lst[i][1] == lst[start][1])
                and lst[i][ind_sort] <= lst[start][ind_sort]):
            j += 1
            lst[i], lst[j] = lst[j], lst[i]

    lst[start], lst[j] = lst[j], lst[start]
    return j


def quick_sort(lst, start, end):
    if start >= end:
        return

    med = choose_median(lst, start, ((start + end) // 2), end)
    j = partition(lst, med, start, end)
    quick_sort(lst, start, j - 1)
    quick_sort(lst, j + 1, end)


students = []
n = int(input())
for _ in range(n):
    name, age = input().split()
    students.append((name, int(age)))

ind_sort = 1
quick_sort(students, 0, n - 1)

ind_sort = 0
quick_sort(students, 0, n - 1)
print("\n".join([name for name, _ in students]))
