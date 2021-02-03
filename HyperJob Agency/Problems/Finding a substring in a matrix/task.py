def contains2d(text, pattern):
    for it in range(nt - np + 1):
        for jt in range(mt - mp + 1):

            found = True
            for ip in range(np):
                for jp in range(mp):
                    if pattern[ip][jp] != text[it + ip][jt + jp]:
                        found = False
                        break
                if not found:
                    break
            if found:
                return True

    return False


nt, mt = [int(d) for d in input().split()]
text_list = []
for _ in range(nt):
    text_list.append(input())

np, mp = [int(d) for d in input().split()]
pat_list = []
for _ in range(np):
    pat_list.append(input())

print(contains2d(text_list, pat_list))
