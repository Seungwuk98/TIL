n, m, b = map(int, input().split())
mat = [list(map(int, input().split()))for _ in range(n)]
INF = int(1e9)


def check(mat, lv, b):
    # lv 걸리는 시간 -> return -> 불가능시에는 아주 큰 값
    sc = 0
    c = 0
    for i in range(n):
        for j in range(m):
            z = mat[i][j] - lv
            if z > 0:
                b += z
                sc += 2*z
            else:
                c += -z
    if b < c:
        return INF
    return sc + c


msc = INF
mlv = 0
for lv in range(256, -1, -1):
    sc = check(mat, lv, b)
    if msc > sc:
        msc = sc
        mlv = lv
print(msc, mlv)
