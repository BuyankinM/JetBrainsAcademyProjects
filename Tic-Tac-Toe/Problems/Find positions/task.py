dig_string = input().split()
dig_find = input()
res_ind = [str(i) for i, c in enumerate(dig_string) if c == dig_find]
if res_ind:
    print(" ".join(res_ind))
else:
    print("not found")