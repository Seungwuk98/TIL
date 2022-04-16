n, m = map(int, input().split())
chess = [input()for _ in range(n)]

w = 'W', 'B'
b = 'B', 'W'


def check(i, j):
    result_w = 0
    result_b = 0
    for di in range(8):
        for dj in range(8):
            ni, nj = i+di, j+dj
            if chess[ni][nj] != w[(di+dj) % 2]:
                result_w += 1
            if chess[ni][nj] != b[(di+dj) % 2]:
                result_b += 1
    return min(result_w, result_b)


result = 10000000
for i in range(n-7):
    for j in range(m-7):
        result = min(result, check(i, j))

print(result)
