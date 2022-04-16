"""
**Instruction**
Please see instruction document.

"""
from BST_Helper import *
from typing import List


def P2(root: TreeNode) -> List[List[int]]:
    ##### Write your Code Here #####
    curr_level = [root]
    ret = []
    while curr_level:
        next_level = []
        curr_val = []
        for curr in curr_level:
            curr_val.append(curr.val)
            if curr.left:
                next_level.append(curr.left)
            if curr.right:
                next_level.append(curr.right)
        ret.append(curr_val)
        curr_level = next_level
    return ret[::-1]

    ##### End of your code #####
