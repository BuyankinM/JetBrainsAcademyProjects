n = int(input())
lists = []
full_len = 0

for _ in range(n):
    cur_list = [int(d) for d in input().split()]
    len_cur_list = len(cur_list)

    lists.append({"list": cur_list, "len": len_cur_list, "ind": 0})
    full_len += len(cur_list)

merged = [0 for _ in range(full_len)]
k = 0

while k < full_len:
    min_val = None
    min_list = 0
    for num_list, cur_list in enumerate(lists):
        cur_val = cur_list["list"][cur_list["ind"]]
        if min_val is None or cur_val < min_val:
            min_val = cur_val
            min_list = num_list

    merged[k] = min_val
    k += 1

    cur_list = lists[min_list]
    cur_list["ind"] += 1

    if cur_list["ind"] == cur_list["len"]:
        del lists[min_list]

print(" ".join([str(d) for d in merged]))
