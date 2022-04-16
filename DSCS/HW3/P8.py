from typing import List


def P8(num_list: List[float]):
    ans_list = []
    ##### Modify code Here #####
    ans_list = [x for x in num_list if x >= 0]
    ##### End of your code #####
    return ans_list
