numbers = [int(d) for d in input()]
print([(numbers[i] + numbers[i + 1]) / 2 for i in range(len(numbers) - 1)])