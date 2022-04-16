def P7(dct: dict) -> int:
    ### Write code here ###
    ky = set()
    for idct in dct.values():
        if not ky:
            ky = {*idct.keys()}
        elif ky != {*idct.keys()}:
            return 0
    return 1

    ### End of your code ###
