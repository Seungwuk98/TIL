def P1(n: int) -> bool:
    # write your code below
    ni = []
    while n:
        ni.append(n & 1)
        n >>= 1
    for i in range(1, len(ni)):
        if ni[i] == ni[i-1]:
            return False
    return True
