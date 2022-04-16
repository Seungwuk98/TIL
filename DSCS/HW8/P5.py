def P5(A: list, B: list) -> int:

    ### Write code here ###
    A.sort()
    B.sort(reverse=True)
    return sum([A[i]*B[i]for i in range(len(A))])
    ### End of your code ###
