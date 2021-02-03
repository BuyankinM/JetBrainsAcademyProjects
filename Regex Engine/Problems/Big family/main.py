# The following lines create dictionaries from the input. Do not modify them, please
first_family = json.loads(input())
second_family = json.loads(input())

new_family = dict()
new_family.update(first_family)
new_family.update(second_family)

print(new_family)