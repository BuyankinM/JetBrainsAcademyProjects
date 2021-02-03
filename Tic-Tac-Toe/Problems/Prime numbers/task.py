prime_numbers = []
for n in range(2, 1000):
    rem = [n % j for j in range(2, n - 1)]
    if all(rem):
        prime_numbers.append(n)