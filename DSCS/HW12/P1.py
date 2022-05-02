def P1(nums: list, k: int) -> bool:
    ### Write code here ###
    bucket = [0]*k
    for x in nums:
        bucket[x % k] += 1
    if bucket[0] & 1:
        return False
    if ~k & 1 and bucket[k >> 1] & 1:
        return False
    for i in range(1, k):
        if bucket[i] != bucket[k-i]:
            return False
    return True
    ### End of your code ###
