from typing import List


def P4(matrix: List[list]) -> List[list]:

    ### Write code here ###
    n = len(matrix)
    m = len(matrix[0])
    nmat = []
    for i in range(1, n+m):
        x, y = 0, m-i
        if y < 0:
            x, y = i-m, 0
        tmp = []
        while 0 <= x < n and 0 <= y < m:
            tmp.append(matrix[x][y])
            x += 1
            y += 1
        nmat.append(tmp)
    for tmp in nmat:
        tmp.sort()

    for i in range(1, n+m):
        x, y = 0, m-i
        if y < 0:
            x, y = i-m, 0
        j = 0
        while 0 <= x < n and 0 <= y < m:
            matrix[x][y] = nmat[i-1][j]
            x += 1
            y += 1
            j += 1
    return matrix

    ### End of your code ###
