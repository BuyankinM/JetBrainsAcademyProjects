from collections import namedtuple

Student = namedtuple("Student", "name len pos")
names = []
num = int(input())

for i in range(num):
    name = input()
    names.append(Student(name, len(name), i))

for i in range(num - 1):
    index = i
    for j in range(i + 1, num):
        if names[j].len < names[index].len \
                or names[j].len == names[index].len and names[j].pos < names[index].pos:
            index = j

    if index != i:
        names[index], names[i] = names[i], names[index]

print("\n".join([stud.name for stud in names]))
