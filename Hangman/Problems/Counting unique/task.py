students = json.loads(input())
Belov = students['Belov']
Smith = students['Smith']
Sarada = students['Sarada']

subjects = set(Belov)
subjects.update(Smith)
subjects.update(Sarada)

print(len(subjects))