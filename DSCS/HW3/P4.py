from typing import List


def P4(word_num_list: List[list]) -> list:
    ans_list = []
    ### Modify code here ###
    for word, length in word_num_list:
        ans_list.append(word)
    ans_list.sort()
    ### End of your code ###
    return ans_list
