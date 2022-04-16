"""
**Instruction**
Please see instruction document.

"""
from BST_Helper import *


def P1(root: TreeNode, low: int, high: int) -> int:
    ret = 0
    if low <= root.val <= high:
        ret += root.val
    if root.right and root.val < high:
        ret += P1(root.right, low, high)
    if root.left and root.val > low:
        ret += P1(root.left, low, high)
    return ret
    ##### End of your code #####
