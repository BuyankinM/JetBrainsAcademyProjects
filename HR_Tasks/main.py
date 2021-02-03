from collections import deque
from pprint import pprint


def minimumMoves(grid, startX, startY, goalX, goalY):
    lg = len(grid)
    l = [[99999] * lg for _ in range(lg)]
    l[startX][startY] = 0

    d = deque([])
    d.append([(startX, startY), None, 0])

    directs = {"left": (0, -1), "right": (0, +1), "up": (-1, 0), "down": (1, 0)}
    while d:
        coord, direct, point = d.popleft()
        for key, value in directs.items():
            X, Y = (coord[0] + value[0]), (coord[1] + value[1])
            p = point + (1 if direct != key else 0)
            if -1 < X < lg and -1 < Y < lg and grid[X][Y] == "." and p <= l[X][Y]:
                d.append([(X, Y), key, p])
                l[X][Y] = p

    return l[goalX][goalY]


grid = """.X..XX...X
X.........
.X.......X
..........
........X.
.X...XXX..
.....X..XX
.....X.X..
..........
.....X..XX""".split("\n")

pprint(["   ".join(list(g)) for g in grid])

startX, startY, goalX, goalY = [int(c) for c in "9 1 9 6".split()]

res = minimumMoves(grid, startX, startY, goalX, goalY)
print(res)
