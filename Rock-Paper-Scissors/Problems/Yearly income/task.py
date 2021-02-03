with open("salary.txt", "r") as fr, \
        open("salary_year.txt", "a") as fw:
    for line in fr:
        print(int(line) * 12, file=fw)
