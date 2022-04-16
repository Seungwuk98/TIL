n = int(input())
arr = [list(map(int, input().split()))for _ in range(n)]
result = [1]*n

for i in range(n):
    for j in range(n):
        if i != j and arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            result[i] += 1

print(' '.join(map(str, result)))
