def P1(n: int) -> bool:
    ##### Write your Code Here #####
    mpf = [*range(n+1)]
    for i in range(2, int(n**0.5)+1):
        if mpf[i] == i:
            for j in range(i*i, n+1, i):
                if mpf[j] == j:
                    mpf[j] = i
    ret = 0
    while n != 1:
        n //= mpf[n]
        ret += 1
    if ret == 2:
        return True
    return False
    ##### End of your code #####
