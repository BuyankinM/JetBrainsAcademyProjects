# read sample.txt and print the number of lines
f = open("test.txt", "r")
for line in f:
    print(line[0])
f.close()