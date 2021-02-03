def search(numbers, target, a, b):
    index = -1

    for ind, elem in enumerate(numbers):
        if ind == b:
            break

        if ind >= a and elem == target:
            index = ind
            break

    return index


nums = [int(d) for d in input().split()]
targ = int(input())
low, high = [int(d) for d in input().split()]

print(search(nums, targ, low, high))
