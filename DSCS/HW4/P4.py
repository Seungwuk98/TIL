def P4(dct: dict) -> str:
    ### Write code here ###

    return max([(val, key) for key, val in dct.items()])[1]

    ### End of your code ###
