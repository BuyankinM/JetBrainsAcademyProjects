def merge_sort(ll: list):
    global num
    if len(ll) == 1:
        return ll

    num += 1
    ind = len(ll) // 2
    res_left = merge_sort(ll[:ind])
    res_right = merge_sort(ll[ind:])


l = [int(d) for d in input().split()]
num = 0
merge_sort(l)
print(num)