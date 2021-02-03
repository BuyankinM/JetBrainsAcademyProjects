def has_suffix(word, suffix):
    result = True

    if len(word) < len(suffix):
        result = False
    else:
        for i in range(-len(suffix), 0):
            if word[i] != suffix[i]:
                result = False
                break

    return result


extension = ".py"
n = int(input())

for i in range(n):
    file = input()
    if has_suffix(file, extension):
        print(file)