from typing import List


def P6(n1: int, n2: int) -> List[int]:
    ans_list = []
    ### Modify code here ###
    if n1 > n2:
        n1, n2 = n2, n1
    ans_list = list(range(n2, n1-1, -1))
    ### End of your code ###
    return ans_list
