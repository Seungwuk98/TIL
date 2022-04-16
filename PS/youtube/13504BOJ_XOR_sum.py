import sys
input = sys.stdin.readline


class Node:
    def __init__(self, lo, hi) -> None:
        self.lo = lo
        self.hi = hi
        self.sum = self.lmax = self.rmax = self.max = 0
        self.left = self.right = None


class SegTree:
    def __init__(self) -> None:
        self.root = self.init(0, n-1)

    def init(self, lo, hi):
        node = Node(lo, hi)
        if lo == hi:
            node.sum = node.lmax = node.rmax = node.max = arr[lo]
            return node
        mid = lo + hi >> 1
        node.left = self.init(lo, mid)
        node.right = self.init(mid+1, hi)
        node.lmax = max(node.left.lmax, node.left.sum ^ node.right.lmax)
        node.rmax = max(node.right.rmax, node.right.sum ^ node.left.rmax)
        node.max = max(node.left.max, node.right.max,
                       node.left.rmax ^ node.right.lmax)
        node.sum = node.left.sum ^ node.right.sum
        return node


for _ in range(int(input())):
    n = int(input())
    arr = [*map(int, input().split())]
    tree = SegTree()
    print(tree.root.max)
