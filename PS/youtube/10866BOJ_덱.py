from collections import deque
import sys
input = sys.stdin.readline

deq = deque()

n = int(input())
for _ in range(n):
    qry = input().split()
    if qry[0] == 'push_back':
        deq.append(qry[1])
    elif qry[0] == 'push_front':
        deq.appendleft(qry[1])
    elif qry[0] == 'pop_back':
        print(deq.pop() if deq else -1)
    elif qry[0] == 'pop_front':
        print(deq.popleft() if deq else -1)
    elif qry[0] == 'size':
        print(len(deq))
    elif qry[0] == 'empty':
        print(0 if deq else 1)
    elif qry[0] == 'front':
        print(deq[0] if deq else -1)
    else:
        print(deq[-1] if deq else -1)
