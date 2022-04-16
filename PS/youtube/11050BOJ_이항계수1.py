from pprint import pprint

C = [[1]*11 for _ in range(11)]
# C[n][k] = nCk
for i in range(1, 11):
    for j in range(1, i):
        C[i][j] = C[i-1][j]+C[i-1][j-1]


n, k = map(int, input().split())

print(C[n][k])
