"""
**Instruction**
Please see instruction document.
"""
from BST_Helper import *


def P3(root: TreeNode, val: int) -> TreeNode:
    ##### Write your Code Here #####
    arr = []

    def inorder(node: TreeNode) -> None:
        if not node:
            return
        inorder(node.left)
        arr.append(node)
        inorder(node.right)
    inorder(root)
    lo, hi = 0, len(arr)
    while lo < hi:
        mid = lo + hi >> 1
        if arr[mid].val < val:
            lo = mid+1
        else:
            hi = mid
    arr.insert(lo, TreeNode(val))

    def rebuild(s: int, e: int) -> TreeNode:
        if s == e:
            arr[s].left = arr[s].right = None
            return arr[s]
        mid = s + e >> 1
        node = arr[mid]
        node.left = rebuild(s, mid-1)
        node.right = rebuild(mid+1, e)
        return node
    root = rebuild(0, len(arr)-1)
    return root

    ##### End of your code #####
