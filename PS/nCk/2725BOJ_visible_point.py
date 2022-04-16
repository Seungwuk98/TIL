from decimal import Decimal

s = set()


def rotate(n):
    n = Decimal(n)
    for i in range(1, int(n)+1):
        s.add(n/i)
    for j in range(0, int(n)):
        s.add(j/n)


t = int(input())
result = [0]*t
qry = []
for i in range(t):
    qry.append((Decimal(input()), i))
qry.sort()

lq, li = qry[0]
for i in range(1, int(lq)+1):
    rotate(i)
result[li] = 1 + len(s)

for w in range(1, t):
    nq, ni = qry[w]
    for i in range(int(lq)+1, int(nq)+1):
        rotate(i)
    result[ni] = 1 + len(s)
    lq, li = nq, ni

print(*result, sep='\n')
