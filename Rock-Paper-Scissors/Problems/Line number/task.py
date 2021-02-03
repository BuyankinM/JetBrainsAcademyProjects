# read sample.txt and print the number of lines
f = open("sample.txt", "r")
print(len(f.readlines()))
f.close()