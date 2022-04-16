import sys
import os
import io
input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
sys.setrecursionlimit(100000)


n = int(input())
size = [1]*(n+1)
parent = [*range(n+1)]
pdist = [0]*(n+1)
depth = [0]*(n+1)
inid = [0]*(n+1)
top = [1]*(n+1)
etov = [0]*n

g = [[]for _ in range(n+1)]
for i in range(1, n):
    a, b, c = map(int, input().split())
    g[a].append((b, c, i))
    g[b].append((a, c, i))


def dfs1(node=1):
    msize = 0
    midx = 0
    for i in range(len(g[node])):
        next, dist, eidx = g[node][i]
        if not visit[next]:
            visit[next] = True
            parent[next] = node
            depth[next] = depth[node] + 1
            etov[eidx] = next
            dfs1(next)
            size[node] += size[next]
            if size[next] > msize:
                msize = size[next]
                midx = i
    g[node][midx], g[node][0] = g[node][0], g[node][midx]


pv = 1


def dfs2(node=1):
    global pv
    inid[node] = pv
    pv += 1
    for i in range(len(g[node])):
        next, dist, eidx = g[node][i]
        if not visit[next]:
            visit[next] = True
            pdist[pv] = dist
            top[next] = top[node] if not i else next
            dfs2(next)


visit = [False]*(n+1)
visit[1] = True
dfs1()
visit = [False]*(n+1)
visit[1] = True
dfs2()


class SegTree:
    def __init__(self) -> None:
        self.tree = [0]*(2*(n+1))
        for i in range(1, n+1):
            self.tree[i+n+1] = pdist[i]
        for i in range(n, 0, -1):
            self.tree[i] = max(self.tree[i << 1], self.tree[i << 1 | 1])

    def query1(self, p, val):
        p = inid[etov[p]]+n+1
        self.tree[p] = val
        while p > 1:
            self.tree[p >> 1] = max(self.tree[p], self.tree[p ^ 1])
            p >>= 1

    def query2(self, l, r):
        result = 0
        r += n+2
        l += n+1
        while l < r:
            if l & 1:
                result = max(result, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                result = max(result, self.tree[r])
            l >>= 1
            r >>= 1
        return result


tree = SegTree()


def query(u, v):
    result = 0
    while top[u] != top[v]:
        if depth[top[u]] < depth[top[v]]:
            u, v = v, u
        st = top[u]
        result = max(result, tree.query2(inid[st], inid[u]))
        u = parent[st]
    if depth[u] > depth[v]:
        u, v = v, u
    if u != v:
        result = max(result, tree.query2(inid[u]+1, inid[v]))
    return result


for _ in range(int(input())):
    q, a, b = map(int, input().split())
    if q == 1:
        tree.query1(a, b)
    else:
        sys.stdout.write('{}\n'.format(query(a, b)))
