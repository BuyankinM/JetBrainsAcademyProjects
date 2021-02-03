f = open("sums.txt", "r")
for line in f:
    print(sum(int(val) for val in line.split()))
f.close()