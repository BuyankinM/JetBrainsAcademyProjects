numbers = [int(d) for d in input()]
print([sum(numbers[:i+1]) for i in range(len(numbers))])