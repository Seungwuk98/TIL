from typing import List
from collections import deque


def P1(rooms: List[list]) -> int:
    ##### Write your Code Here #####
    n = len(rooms)
    m = len(rooms[0])
    d = (0, 1), (1, 0), (0, -1), (-1, 0)
    fill = True
    q = deque()
    for i in range(n):
        for j in range(m):
            if rooms[i][j] == 1:
                q.append((i, j, 0))
            elif rooms[i][j] == 0:
                fill = False
    if fill:
        return 0

    while q:
        x, y, count = q.popleft()
        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and rooms[nx][ny] == 0:
                rooms[nx][ny] = count+1
                q.append((nx, ny, count+1))
    for i in range(n):
        for j in range(m):
            if not rooms[i][j]:
                return -1
    return max([max(x)for x in rooms])
    ##### End of your code #####
