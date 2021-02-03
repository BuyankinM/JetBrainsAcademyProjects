d = int(input())
prime = (d > 1)
for n in range(2, int(d ** 0.5) + 1):
    if not d % n:
        prime = False
        break
if prime:
    print("This number is prime")
else:
    print("This number is not prime")