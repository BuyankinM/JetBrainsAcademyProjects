def search(numbers, target):
    index = -1

    for ind, elem in enumerate(numbers):
        if elem == target:
            index = ind

    return index

nums = [int(d) for d in input().split()]
targ = int(input())
print(search(nums, targ))