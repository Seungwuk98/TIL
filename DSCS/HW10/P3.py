"""
**Instruction**
Please see instruction document.
"""
from BST_Helper import *


def P3(root: TreeNode, val: int) -> TreeNode:
    ##### Write your Code Here #####
    def fillLeafNode(currNode: TreeNode) -> None:
        # 비어있는 리프노드를 채워줍니다.
        if currNode:
            if currNode.left and not currNode.right:
                currNode.right = TreeNode(None)
            if currNode.right and not currNode.left:
                currNode.left = TreeNode(None)
            fillLeafNode(currNode.left)
            fillLeafNode(currNode.right)
    fillLeafNode(root)

    def setNoneRightLeaf(currNode: TreeNode) -> TreeNode:
        # 리프노드에 있는 None 값을 가장 오른쪽 리프노드로 밀어줍니다.
        if not currNode.left and not currNode.right:
            # 리프노드인 경우 종료
            return None
        if currNode.left.val == None:
            # 왼쪽 값이 비어있으면 값을 왼쪽으로 밀어줍니다.
            currNode.left.val, currNode.val = currNode.val, currNode.left.val
            currNode.right.val, currNode.val = currNode.val, currNode.right.val
        if currNode.right.val == None:
            # 오른쪽 노드가 비어있으면 해당 노드를 반환합니다.
            return currNode.right
        # left 노드를 순환하여 None 노드를 가져옵니다.
        markedNodeLeft = setNoneRightLeaf(currNode.left)
        if markedNodeLeft:
            # None노드를 가져오면, 현재 노드, 오른쪽 서브트리 가장 작은 노드
            # 셋이서 값을 왼쪽으로 밀어줍니다. 오른쪽 서브트리 가장 작은 노드가 None이 됩니다.
            RmaxNode = currNode.right
            while RmaxNode.left:
                RmaxNode = RmaxNode.left
            markedNodeLeft.val, currNode.val = currNode.val, markedNodeLeft.val
            currNode.val, RmaxNode.val = RmaxNode.val, currNode.val
        markedNodeRight = setNoneRightLeaf(currNode.right)
        # right 노드를 순회하여 받아온게 있다면 그것을 리턴합니다.
        return markedNodeRight if markedNodeRight else markedNodeLeft
    setNoneRightLeaf(root)
    global tmp
    tmp = val

    def inorder(currNode):
        # 중위 순회 하며, 값을 하나씩 밀어줍니다.
        global tmp
        if currNode:
            inorder(currNode.left)
            if currNode.val == None or tmp < currNode.val:
                currNode.val, tmp = tmp, currNode.val
            inorder(currNode.right)
    inorder(root)
    return root


sample_case = [
    [[7, 3, 8, 2, 5, None, 9], 6],
    [[7, 3, 8, 2, 5, None, 9], 10],
    [[10, 5, 15, 3, 6, 12, 18, 1, 4, None, 8, 11, 13, 16, 20], 7],
    [[10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, None, 20], 14],
    [[10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, None, 20], 9],
    [[7, 6, None], 10],
    [[7, 6, None], 5],
    [[100, 50, 150, 25, 75, 125, 175, 12, 40, 62, 90, 112, 140, 162, 190, 6, 18,
        34, 46, 56, 68, 84, 96, 106, 120, 130, None, 156, 168, 184, 196], 145],
    [[100, 50, 150, 25, 75, 125, 175, 12, 40, 62, 90, 112, 140, 162, 190, 6,
        18, 34, 46, 56, 68, 84, 96, 106, 120, 130, None, 156, 168, 184, 196], 28],
    [[100, 50, 150, 25, 75, 125, 175, 12, 40, 62, 90, 112, 140, 162, 190, 6,
        18, 34, 46, 56, 68, 84, 96, 106, 120, 130, None, 156, 168, 184, 196], 200]
]


for x, y in sample_case:
    root = create_linked_bst(x)
    fullBST = P3(root, y)
    print(fullBST.printTree())


# root = create_linked_bst([7, 3, 8, 2, 5, None, 9])
# fullBST = P3(root, 6)
# print(fullBST.printTree())
# # root_print(fullBST)

# root = create_linked_bst([7, 3, 8, 2, 5, None, 9])
# fullBST = P3(root, 10)
# print(fullBST .printTree())
# # root_print(fullBST)

# root = create_linked_bst(
#     [10, 5, 15, 3, 6, 12, 18, 1, 4, None, 8, 11, 13, 16, 20])
# fullBST = P3(root, 7)
# print(fullBST .printTree())

# root = create_linked_bst(
#     [10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, None, 20])
# fullBST = P3(root, 14)
# print(fullBST .printTree())

# root = create_linked_bst(
#     [10, 5, 15, 3, 7, 12, 18, 1, 4, 6, 8, 11, 13, None, 20])
# fullBST = P3(root, 9)
# print(fullBST .printTree())
