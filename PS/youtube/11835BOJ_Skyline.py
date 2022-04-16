n = int(input())
arr = [*map(int, input().split())]
a, b, c = 0, 0, 0
cnt = 0
for i in range(n):
    t = min(a, arr[i])
    cnt += 2*t
    c = min(arr[i]-t, b)
    cnt += 2*c
    a = arr[i]-t-c
    cnt += 3*a
    b = t
print(cnt)
