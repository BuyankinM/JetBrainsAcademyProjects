n = int(input())
percent = 7.1
years = 0

while n < 700_000:
    n += n * percent / 100
    years += 1

print(years)