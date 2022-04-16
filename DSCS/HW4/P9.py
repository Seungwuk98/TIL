def P9(dct1: dict, dct2: dict) -> int:
    ### Write code here ###
    ret = 0
    for key in dct1:
        if key in dct2:
            ret += dct1[key] * dct2[key]
    return ret

    ### End of your code ###
