from decimal import *
from math import *


def mat_cross(a, b):
    ret = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                ret[i][j] += a[i][k] * b[k][j]
                ret[i][j] %= 1000
    return ret


def mat_pow(c, n):
    ret = [[1, 0], [0, 1]]
    while n:
        if n & 1:
            ret = mat_cross(ret, c)
        c = mat_cross(c, c)
        n >>= 1
    return ret


for _ in range(int(input())):
    n = int(input())
    if n == 1:
        X = 5
    elif n == 2:
        X = 27
    else:
        X = [[6, -4], [1, 0]]
        X = mat_pow(X, n-2)
        C = 28*X[0][0] + 6*X[0][1]
        X = (int(C)-1) % 1000

    print('Case #{0:}: {1:0>3}'.format(_+1, X))
