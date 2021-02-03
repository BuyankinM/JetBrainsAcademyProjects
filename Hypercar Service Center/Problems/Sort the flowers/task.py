# the following line creates a list from the input, do not modify it, please
prices = [float(price.strip(" ,")) for price in input().split()]
prices = [int(pr) if pr == int(pr) else pr for pr in prices]

print(list(sorted(prices, reverse=True)))