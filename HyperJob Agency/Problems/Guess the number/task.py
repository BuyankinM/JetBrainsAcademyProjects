x = int(input())
lx, rx = (int(n) for n in input().split())
tries = 0

ll = list(range(lx, rx + 1))

while lx <= rx:
    mid = (lx + rx) // 2
    tries += 1

    mid_elem = ll[mid-1]
    if mid_elem == x:
        break
    elif x > mid_elem:
        lx = mid + 1
    else:
        rx = mid - 1

print(tries)