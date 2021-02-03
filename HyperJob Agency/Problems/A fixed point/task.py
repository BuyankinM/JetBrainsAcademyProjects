l = [int(d) for d in input().split()]

lx, rx = 0, len(l) - 1
result = False

while lx <= rx:
    mid = (lx + rx) // 2
    elem_mid = l[mid]

    if mid == elem_mid:
        result = True
        break
    elif mid > elem_mid:
        lx = mid + 1
    else:
        rx = mid - 1

print(result)
