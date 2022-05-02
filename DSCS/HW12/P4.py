def P4(nums: list) -> int:

    ### Write code here ###
    s = set(nums)
    ret = 1
    vst = {x: False for x in s}
    for num in s:
        if not vst[num]:
            vst[num] = True
            cnt = 1
            tmp = num
            while tmp+1 in s and not vst[tmp+1]:
                tmp += 1
                cnt += 1
                vst[tmp] = True
            tmp = num
            while tmp-1 in s and not vst[tmp-1]:
                tmp -= 1
                cnt += 1
                vst[tmp] = True
            ret = max(ret, cnt)
    return ret
    ### End of your code ###
