def P3(A: list, B: list) -> int:

    ### Write code here ###
    n = len(A)
    d = {0: -1}
    now = 0
    ret = 0
    for i in range(n):
        now += A[i] - B[i]
        if now in d:
            ret = max(i-d[now], ret)
        else:
            d[now] = i
    return ret
    ### End of your code ###
