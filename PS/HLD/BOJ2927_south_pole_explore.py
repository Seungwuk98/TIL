import sys
input = sys.stdin.readline
sys.setrecursionlimit(30030)
n = int(input())
parent = [*range(n)]
g = [[]for _ in range(n)]
arr = [*map(int, input().split())]
rank = [0]*n


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    r1, r2 = find(node1), find(node2)
    if r1 == r2:
        return 'no'
    if rank[r1] > rank[r2]:
        parent[r2] = r1
    else:
        parent[r1] = r2
        if rank[r1] == rank[r2]:
            rank[r2] += 1
    return 'yes'


query = []
q = int(input())
for _ in range(q):
    q, a, b = input().split()
    a, b = int(a)-1, int(b)
    if q == 'excursion':
        b -= 1
        if find(a) != find(b):
            q = 'impossible'
    elif q == 'bridge':
        b -= 1
        q = union(a, b)
        if q == 'yes':
            g[a].append(b)
            g[b].append(a)
    query.append((q, a, b))

for x in set(parent):
    if x:
        g[0].append(x)

iin = [0]*n
top = [0]*n
depth = [0]*n
size = [1]*n

bit = [0]*(n+1)


def update(i, v):
    i += 1
    while i <= n:
        bit[i] += v
        i += i & -i


def isum(l, r):
    r += 1
    ret = 0
    while r:
        ret += bit[r]
        r -= r & -r
    while l:
        ret -= bit[l]
        l -= l & -l
    return ret


def dfs1(node=0):
    midx = 0
    msz = 0
    for i in range(len(g[node])):
        next = g[node][i]
        if not visit[next]:
            visit[next] = True
            parent[next] = node
            depth[next] = depth[node]+1
            dfs1(next)
            size[node] += size[next]
            if size[next] > msz:
                msz = size[next]
                midx = i
    if g[node]:
        g[node][0], g[node][midx] = g[node][midx], g[node][0]


pv = 0


def dfs2(node=0):
    global pv
    iin[node] = pv
    update(pv, arr[node])
    pv += 1
    for i in range(len(g[node])):
        next = g[node][i]
        if not visit[next]:
            visit[next] = True
            top[next] = next if i else top[node]
            dfs2(next)


visit = [False]*n
visit[0] = True
dfs1()
visit = [False]*n
visit[0] = True
dfs2()


def excursion(a, b):
    ret = 0
    while top[a] != top[b]:
        if depth[top[a]] < depth[top[b]]:
            a, b = b, a
        st = top[a]
        ret += isum(iin[st], iin[a])
        a = parent[st]
    if depth[a] > depth[b]:
        a, b = b, a
    ret += isum(iin[a], iin[b])
    return ret


for q, a, b in query:
    if q == 'yes' or q == 'no' or q == 'impossible':
        sys.stdout.write(q+'\n')
    elif q == 'excursion':
        sys.stdout.write(str(excursion(a, b))+'\n')
    elif q == 'penguins':
        update(iin[a], b - arr[a])
        arr[a] = b
