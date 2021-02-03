def has_prefix(word, prefix):
    result = True
    for i, c in enumerate(prefix):
        if word[i] != c:
            result = False
            break
    return result


prefix = input()
words = input().split()

for word in words:
    if has_prefix(word, prefix):
        print(word)