n = int(input())
i = 0
while i*3 <= n:
    q, r = divmod(n-3*i, 5)
    if not r:
        break
    i += 1
else:
    print(-1)
    exit(0)
print(i+q)
