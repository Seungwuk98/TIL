def P2(Order: str, S: str) -> str:

    ### Write code here ###
    Ol = len(Order)
    d = {Order[i]: i for i in range(Ol)}
    bucket = [0]*Ol
    retright = ''
    for x in S:
        if x in d:
            bucket[d[x]] += 1
        else:
            retright += x
    retleft = ''
    for i in range(Ol):
        while bucket[d[Order[i]]]:
            retleft += Order[i]
            bucket[d[Order[i]]] -= 1
    return retleft + retright
    ### End of your code ###
