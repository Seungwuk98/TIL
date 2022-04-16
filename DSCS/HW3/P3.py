from typing import List


def P3(num_list: List[int]) -> List[int]:
    ans_list = []
    ### Modify code here ###
    for x in num_list:
        ans_list.append(-x)
    ### End of your code ###
    return ans_list
