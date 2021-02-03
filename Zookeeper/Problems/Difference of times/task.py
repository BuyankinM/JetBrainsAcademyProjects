hour_1, minute_1, second_1 = int(input()), int(input()), int(input())
hour_2, minute_2, second_2 = int(input()), int(input()), int(input())
print(3600 * hour_2 + 60 * minute_2 + second_2 - 3600 * hour_1 - 60 * minute_1 - second_1)