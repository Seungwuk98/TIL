from typing import List
from collections import deque


def P4(world: List[list]) -> int:
    ##### Write your Code Here #####
    n = len(world)
    m = len(world[0])
    vst = [[False]*m for _ in range(n)]
    d = (1, 0), (0, -1), (-1, 0), (0, 1)
    count = 0
    for i in range(n):
        for j in range(m):
            if not vst[i][j] and world[i][j]:
                vst[i][j] = True
                count += 1
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in d:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < m and not vst[nx][ny] and world[nx][ny]:
                            vst[nx][ny] = True
                            q.append((nx, ny))
    return count
