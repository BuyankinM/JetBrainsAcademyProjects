s = input()
for c in s:
    if not c.isalpha():
        break
    if c in "aeiou":
        print("vowel")
    else:
        print("consonant")