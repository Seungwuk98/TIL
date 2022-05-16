def P3(nums: list) -> set:
    # write your code below
    s = 0
    l = 0
    r = 0
    for x in nums:
        s ^= x
    y = s & -s
    for x in nums:
        if x & y:
            l ^= x
        else:
            r ^= x
    return {l, r}
