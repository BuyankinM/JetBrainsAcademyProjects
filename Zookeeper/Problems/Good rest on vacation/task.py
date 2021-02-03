days, food_cost, flight_cost, hotel_cost = int(input()), int(input()), int(input()), int(input())
print(days * food_cost + (days - 1) * hotel_cost + 2 * flight_cost)