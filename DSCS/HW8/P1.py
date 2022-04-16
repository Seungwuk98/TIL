def P1(num_list: list) -> int:

    ### Write code here ###
    n = len(num_list)
    ret = 0
    for i in range(n-1):
        for j in range(n-i-1):
            if num_list[j] > num_list[j+1]:
                num_list[j], num_list[j+1] = num_list[j+1], num_list[j]
                ret += 1
    return ret

    ### End of your code ###
