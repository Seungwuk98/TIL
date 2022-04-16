from collections import deque
from typing import List


def P3(image: List[list]) -> int:
    ##### Write your Code Here #####
    n = len(image)
    m = len(image[0])
    vst = [[False]*m for _ in range(n)]
    d = (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)
    count = 0
    for i in range(n):
        for j in range(m):
            if not vst[i][j] and image[i][j]:
                vst[i][j] = True
                count += 1
                q = deque([(i, j)])
                while q:
                    x, y = q.popleft()
                    for dx, dy in d:
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < n and 0 <= ny < m and not vst[nx][ny] and image[nx][ny]:
                            vst[nx][ny] = True
                            q.append((nx, ny))
    return count
    ##### End of your code #####
