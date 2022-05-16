def P2(num: int) -> int:
    # write your code below
    ni = []
    for _ in range(32):
        ni.append(num & 1)
        num >>= 1
    ni = ni[::-1]
    ret, c = 0, 1
    for i in range(32):
        ret += c * ni[i]
        c <<= 1
    return ret
