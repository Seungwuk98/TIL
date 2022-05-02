from typing import List


d = {}

def sol(list : List[int]) -> int:
    n = len(list)
    for x in list:
        if x not in d:
            d[x] = 1
        else:
            d[x] +=1
        if d[x] > (n>>1):
            return x
    