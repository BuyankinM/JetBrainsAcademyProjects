from colorama import Fore, Back, Style, init


def print_dates(word=None, start_end=None):
    if word is None:
        print(" ".join([str(d) for d in dates]))
    elif start_end is None:
        print(word, " ".join([str(d) for d in dates]))
    else:
        print(word, end=" ")
        for i, num in enumerate(dates):
            add_color = Fore.RED if i in start_end else Fore.BLACK
            print(add_color + str(num), end=" ")
    print(Style.RESET_ALL)


def partition_old(lst, start, end):
    j = start
    for i in range(start + 1, end + 1):
        if lst[i] <= lst[start]:
            j += 1
            if i != j:
                lst[i], lst[j] = lst[j], lst[i]
                print_dates("swap", (i, j))
    lst[start], lst[j] = lst[j], lst[start]
    print_dates("end ", (start, j))
    return j


def partition(lst, start, end):
    x = lst[start]
    m1 = start
    m2 = start

    for i in range(start + 1, end + 1):
        if lst[i] > x:
            lst[i], lst[m1] = lst[m1], lst[i]
            lst[i], lst[m2 + 1] = lst[m2 + 1], lst[i]
            m1 += 1
            m2 += 1
        elif lst[i] == x:
            lst[i], lst[m2 + 1] = lst[m2 + 1], lst[i]
            m2 += 1
    return m1, m2


def quick_sort(lst, start, end):
    if start >= end:
        return

    j, k = partition(lst, start, end)
    quick_sort(lst, start, j - 1)
    quick_sort(lst, k + 1, end)


init()
dates = list(map(int, input().split()))
quick_sort(dates, 0, len(dates) - 1)
print_dates()
