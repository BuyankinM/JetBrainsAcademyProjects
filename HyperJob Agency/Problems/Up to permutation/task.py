def contains_upto_permutations(text, pattern):
    result = False

    for i in range(len(text) - len(pattern) + 1):
        indexes = set()
        for j in range(len(pattern)):
            found_ct = False
            ct = text[i + j]
            for ind, cp in enumerate(pattern):
                if ind not in indexes and cp == ct:
                    indexes.add(ind)
                    found_ct = True
                    break

            if not found_ct:
                break

        if len(indexes) == len(pattern):
            result = True
            break

    print(result)

contains_upto_permutations(input(), input())
