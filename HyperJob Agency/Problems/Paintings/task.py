n, w, h = (int(d) for d in input().split())
s_min = n * w * h

# frames = [5, 6, 7, 8, 9]

lx = 0
rx = len(frames) - 1
index = -1

while lx <= rx:
    mid = (lx + rx) // 2

    mid_elem = frames[mid] ** 2
    if mid_elem == s_min:
        index = mid
        break
    elif s_min > mid_elem:
        lx = mid + 1
    else:
        index = mid
        rx = mid - 1

print(max(0, index))
