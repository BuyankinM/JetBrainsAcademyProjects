def binary_search(numbers, target):
    lx = 0
    rx = len(numbers) - 1
    index = -1

    while lx <= rx:
        mid = (lx + rx) // 2

        mid_elem = numbers[mid]
        if mid_elem == target:
            index = mid
            break
        elif target > mid_elem:
            lx = mid + 1
        else:
            rx = mid - 1

    return index


l_search = [int(d) for d in input().split()]
l_main = [int(d) for d in input().split()]

for el in l_search:
    print(binary_search(l_main, el), end=" ")