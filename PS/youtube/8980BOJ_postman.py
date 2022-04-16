def u(): return map(int, input().split())


n, c = u()
m = int(input())
tk = [c]*(n+1)
ret = 0
for s, e, w in [[*u()]for _ in [0]*m]:
    mn = min(*tk[s:e], w)
    ret += mn
    for i in range(s, e):
        tk[i] -= mn
print(ret)
