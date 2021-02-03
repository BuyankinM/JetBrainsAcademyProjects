def count(numbers, target):
    n = 0

    for elem in numbers:
        if elem == target:
            n += 1

    return n


nums = [int(d) for d in input().split()]
targ = int(input())
print(count(nums, targ))