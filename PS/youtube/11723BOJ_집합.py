import sys
input = sys.stdin.readline

s = 0
all = (1 << 20)-1
for _ in range(int(input())):
    qry = list(input().split())
    if len(qry) == 2:
        qry[1] = int(qry[1])-1

    if qry[0] == 'add':
        s |= 1 << qry[1]
    elif qry[0] == 'remove':
        s &= ~(1 << qry[1])
    elif qry[0] == 'check':
        print(1 if s & (1 << qry[1]) else 0)
    elif qry[0] == 'toggle':
        s ^= 1 << qry[1]
    elif qry[0] == 'all':
        s = all
    else:
        s = 0
