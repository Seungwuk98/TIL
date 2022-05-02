def P2(nums: list) -> int:

    ### Write code here ###
    n = len(nums)
    now = 0
    d = {0: -1}
    ret = 0
    for i in range(n):
        now += 1 if nums[i] else -1
        if now not in d:
            d[now] = i
        else:
            ret = max(ret, i-d[now])
    return ret
    ### End of your code ###
