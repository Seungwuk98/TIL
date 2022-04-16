mat = [list(map(int, input().split()))for _ in range(9)]

vst1 = [[False]*9 for _ in range(9)]
# vst1[i][j] -> i번 행에 j가 들어가 있는가?
vst2 = [[False]*9 for _ in range(9)]
# vst2[i][j] -> i번 열에 j가 들어가 있는가?
vst3 = [[False]*9 for _ in range(9)]
# vst3[i][j] -> i번 박스에 j가 들어가 있는가?


def box(i, j):
    return i//3*3+j//3


for i in range(9):
    for j in range(9):
        if mat[i][j]:
            vst1[i][mat[i][j]-1] = True
            vst2[j][mat[i][j]-1] = True
            vst3[box(i, j)][mat[i][j]-1] = True


def back(i, j):
    if i == 9:
        return True

    if mat[i][j]:
        return back(i+(j+1)//9, (j+1) % 9)

    for k in range(9):
        if vst1[i][k] or vst2[j][k] or vst3[box(i, j)][k]:
            continue
        mat[i][j] = k+1
        vst1[i][k] = vst2[j][k] = vst3[box(i, j)][k] = True
        if back(i+(j+1)//9, (j+1) % 9):
            return True
        mat[i][j] = 0
        vst1[i][k] = vst2[j][k] = vst3[box(i, j)][k] = False
    return False


back(0, 0)
for x in mat:
    print(*x)

# 후보 ( 1 3 4 )

# 0 0  -> 0 8
# 1 0  -> 1 8

# 8 8
# 9 0

# 행 별로 ->
# 열 별로 들어가 있는 숫자 ->
# 박스 별로 ->
