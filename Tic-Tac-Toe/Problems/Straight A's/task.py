grade_string = "".join(input().split())
print(round(grade_string.count("A") / len(grade_string), 2))