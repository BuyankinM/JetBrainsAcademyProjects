year = int(input())

if (not year % 4 and year % 100) or (not year % 400):
    print("Leap")
else:
    print("Ordinary")