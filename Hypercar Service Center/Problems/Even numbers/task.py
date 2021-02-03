n = int(input())


def even():
    for i in range(0, 2 * n, 2):
        yield i


for ee in even():
    print(ee)