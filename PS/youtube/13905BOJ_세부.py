from heapq import *
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
s, e = map(int, input().split())
g = [[]for _ in range(n+1)]
for _ in range(m):
    h1, h2, k = map(int, input().split())
    g[h1].append((k, h2))
    g[h2].append((k, h1))

heap = [(-10000000, s)]
distance = [-1]*(n+1)
while heap:
    pp, now = heappop(heap)
    pp = -pp
    for weight, next in g[now]:
        from_start = min(weight, pp)
        if from_start > distance[next]:
            distance[next] = from_start
            heappush(heap, (-from_start, next))

if distance[e] == -1:
    print(0)
else:
    print(distance[e])
