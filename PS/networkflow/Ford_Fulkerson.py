from collections import deque
from functools import singledispatch

INF = int(1e9)
v = 1000
capacity = [[0]*1000 for _ in range(1000)]
flow = [[0]*1000 for _ in range(1000)]


def networkflow(source, sink):
    totalFlow = 0
    while 1:
        parent = [-1]*(1000)
        q = deque()
        parent[source] = source
        q.append(source)
        while q and parent[sink] == -1:
            here = q.popleft()
            for there in range(v):
                if (capacity[here][there] - flow[here][there] > 0 and parent[there] == -1):
                    q.append(there)
                    parent[there] = here
        if parent[sink] == -1:
            break
        amount = INF
        p = sink
        while p != source:
            amount = min(amount, capacity[parent[p]][p] - flow[parent[p]][p])
        p = sink
        while p != source:
            flow[parent[p]][p] += amount
            flow[p][parent[p]] -= amount
        totalFlow += amount
    return totalFlow
