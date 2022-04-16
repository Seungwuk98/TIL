from typing import List


def P5(alphabet_list: List[str]) -> int:
    idx = 0
    ### Modify code here ###
    for i in range(len(alphabet_list)):
        if 'A' <= alphabet_list[i] <= 'Z':
            return i
    idx = -1
    ### End of your code ###
    return idx
