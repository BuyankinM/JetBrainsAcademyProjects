# read animals.txt
f_animals = open("animals.txt", "r")
f_new = open("animals_new.txt", "a")

for line in f_animals:
    f_new.write(line.strip() + " ")

f_animals.close()
f_new.close()