import sys
input = sys.stdin.readline
def ii(): return map(int, input().split())


def print(x): return sys.stdout.write('{}\n'.format(x))


n, q = ii()
sn = int(n**0.5)+1
arr = [*ii()]
qry = []
for i in range(q):
    a, b = ii()
    qry.append((a-1, b-1, i))
qry.sort(key=lambda x: (x[0]//sn, x[1]))

result = [0]*q
now = [0]*(200001)
mmax = [0]*(n+1)
mmax[0] = n
rmax = 0


def insert(x):
    global rmax
    y = arr[x]
    mmax[now[y]] -= 1
    now[y] += 1
    mmax[now[y]] += 1
    rmax = max(rmax, now[y])


def delete(x):
    global rmax
    y = arr[x]
    mmax[now[y]] -= 1
    if rmax == now[y] and not mmax[now[y]]:
        rmax -= 1
    now[y] -= 1
    mmax[now[y]] += 1


ll, lr, lk = qry[0]
for x in range(ll, lr+1):
    insert(x)
result[lk] = rmax

for w in range(1, q):
    nl, nr, nk = qry[w]
    if nl//sn == ll//sn:
        for x in range(lr+1, nr+1):
            insert(x)
        if nl < ll:
            for x in range(nl, ll):
                insert(x)
        else:
            for x in range(ll, nl):
                delete(x)
    else:
        if lr < nr:
            for x in range(lr+1, nr+1):
                insert(x)
        else:
            for x in range(nr+1, lr+1):
                delete(x)
        for x in range(ll, nl):
            delete(x)
    result[nk] = rmax
    ll, lr, lk = nl, nr, nk

for x in result:
    print(x)
