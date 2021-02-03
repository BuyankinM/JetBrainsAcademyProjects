def find_last(text, pattern):
    ind = -1
    for i in range(len(text) - len(pattern) + 1):
        found = True

        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                found = False
                break

        if found:
            ind = i

    print(ind)

find_last(input(), input())