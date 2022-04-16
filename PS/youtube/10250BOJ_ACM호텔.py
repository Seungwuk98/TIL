t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    q, r = divmod(n-1, h)
    print((r+1)*100+q+1)
