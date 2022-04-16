n = int(input())
mat = [[*map(int, input().split())]for _ in range(n)]


def chk(mat, i, j, sz):
    c = mat[i][j]
    for x in range(i, i+sz):
        for y in range(j, j+sz):
            if mat[x][y] != mat[i][j]:
                return False
    return True


def solve(mat, i, j, sz):
    if not sz:
        return 0, 0
    if chk(mat, i, j, sz):
        return (1, 0) if mat[i][j] else (0, 1)
    hf = sz >> 1
    retb, retw = 0, 0
    for x in (i, i+hf):
        for y in (j, j+hf):
            b, w = solve(mat, x, y, hf)
            retb += b
            retw += w
    return retb, retw


retb, retw = solve(mat, 0, 0, n)
print(retw, retb)
