from collections import deque
from typing import List


def P2(n: int, edges: List[tuple]) -> int:
    ##### Write your Code Here #####
    g = [[]for _ in range(n+1)]
    for x, y in edges:
        g[x].append(y)
        g[y].append(x)
    vst = [False]*(n+1)
    vst[1] = True
    q = deque([1])
    count = 0
    while q:
        now = q.popleft()
        count += 1
        for nxt in g[now]:
            if not vst[nxt]:
                vst[nxt] = True
                q.append(nxt)
    return count
    ##### End of your code #####
