numbers = [int(n) for n in input()]

less_than_5 = [a for a in numbers if a < 5]
greater_than_5 = [a for a in numbers if a > 5]

print(less_than_5)
print(greater_than_5)