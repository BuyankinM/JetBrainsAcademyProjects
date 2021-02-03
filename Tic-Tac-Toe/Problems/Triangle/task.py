n = int(input())
max_len = 2 * n - 1
print("\n".join([("#" * i).center(max_len) for i in range(1, max_len + 1, 2)]))