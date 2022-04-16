n, x, p = map(int, input().split())
arr = [-1]*p
if n:
    arr = [*map(int, input().split())]+[-1]*(p-n)

i = 0
while i < p:
    if arr[i] < x:
        break
    i += 1

if i == p:
    print(-1)
else:
    arr.insert(i, x)
    result = [1]*p
    for j in range(1, p+1):
        result[j-1] = j
        if j and arr[j-1] == arr[j-2]:
            result[j-1] = result[j-2]
    print(result[i])
