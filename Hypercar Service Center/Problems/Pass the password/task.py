# the follwing line reads the list from the input, do not modify it, please
passwords = input().split()

passwords.sort(key=len)
for pas in passwords:
    print(pas, len(pas))