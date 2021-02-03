def kth(numbers, target, k):
    index = -1

    for ind, elem in enumerate(numbers):
        if elem == target:
            k -= 1
            if not k:
                index = ind
                break

    return index


nums = [int(d) for d in input().split()]
targ = int(input())
kk = int(input())

print(kth(nums, targ, kk))