import sys
from collections import deque
input = sys.stdin.readline


q = deque()

n = int(input())
for _ in range(n):
    qry = input().split()
    if qry[0] == 'push':
        q.append(qry[1])
    elif qry[0] == 'pop':
        print(q.popleft() if q else -1)
    elif qry[0] == 'size':
        print(len(q))
    elif qry[0] == 'empty':
        print(0 if q else 1)
    elif qry[0] == 'front':
        print(q[0] if q else -1)
    else:
        print(q[-1] if q else -1)
