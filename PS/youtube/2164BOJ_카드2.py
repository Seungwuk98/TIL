from collections import deque
n = int(input())
q = deque(range(1, n+1))
exec('q.popleft();q.append(q.popleft());'*(n-1))
print(q[0])
