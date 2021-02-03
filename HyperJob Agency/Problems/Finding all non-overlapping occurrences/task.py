def find_no_overlaps(text, pattern):

    i = 0
    ind = -1
    len_pat = len(pattern)
    len_text = len(text)

    while i <= (len_text - len_pat):
        found = True

        for j in range(len_pat):
            if text[i + j] != pattern[j]:
                found = False
                break

        if found:
            ind = i
            i += len_pat
            print(ind, end=" ")
        else:
            i += 1

    if ind == -1:
        print(ind)

find_no_overlaps(input(), input())