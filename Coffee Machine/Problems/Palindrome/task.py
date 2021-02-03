s = input()
ss = ""
for c in range(-1, -1 * len(s) - 1, -1):
    ss += s[c]

if s == ss:
    print("Palindrome")
else:
    print("Not palindrome")