from collections import deque

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = list(map(int, input().split()))
    q = deque()
    for i, x in enumerate(s):
        q.append((i, x))
    s.sort()
    count = 0
    while q:
        i, x = q.popleft()
        if x == s[-1]:
            s.pop()
            count += 1
            if i == m:
                print(count)
                break
        else:
            q.append((i, x))
