def P5(dct: dict) -> list:
    ### Write code here ###
    ret = []
    st1 = set()
    for val in dct.values():
        if val not in st1:
            st1.add(val)
        else:
            ret.append(val)
    return ret

    ### End of your code ###
