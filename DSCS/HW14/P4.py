def P4(num: int) -> int:
    # write your code below
    ni = []
    while num:
        ni.append(num & 1)
        num >>= 1
    return sum(ni)
