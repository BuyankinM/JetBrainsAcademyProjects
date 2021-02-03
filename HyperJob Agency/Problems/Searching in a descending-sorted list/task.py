def binary_search(elements, target):
    left, right = 0, len(elements) - 1

    index = -1
    while left <= right:
        middle = (left + right) // 2

        if elements[middle] == target:
            index = middle
            right = middle - 1
        if target < elements[middle]:
            left = middle + 1
        else:
            right = middle - 1

    return index

l = [int(d) for d in input().split()]
x = int(input())

print(binary_search(l, x))