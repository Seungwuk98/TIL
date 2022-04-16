import sys
input = sys.stdin.readline
INF = 1 << 31-1


class Node:
    def __init__(self) -> None:
        self.left = self.right = None
        self.cnt = 0


class Segtree:
    def __init__(self) -> None:
        self.tree = Node()

    def update(self, node, lo, hi, w):
        if lo == hi:
            node.cnt += 1
            return
        mid = lo + hi >> 1
        if w <= mid:
            if not node.left:
                node.left = Node()
            self.update(node.left, lo, mid, w)
        else:
            if not node.right:
                node.right = Node()
            self.update(node.right, mid+1, hi, w)
        node.cnt = (node.left.cnt if node.left else 0) + \
            (node.right.cnt if node.right else 0)

    def query(self, node, lo, hi, k):
        if lo == hi:
            return lo
        mid = lo + hi >> 1
        diff = node.left.cnt if node.left else 0
        if k > diff:
            return self.query(node.right, mid+1, hi, k-diff)
        else:
            return self.query(node.left, lo, mid, k)


for _ in range(int(input())):
    tree = Segtree()
    result = []
    cnt = 0
    n = int(input())
    arr = []
    for i in range((n-1)//10+1):
        arr.extend([*map(int, input().split())])
    for x in arr:
        tree.update(tree.tree, -INF-1, INF, x)
        cnt += 1
        if cnt & 1:
            result.append(tree.query(tree.tree, -INF-1, INF, cnt//2+1))
    print(len(result))
    p = []
    for i in range(len(result)):
        p.append(result[i])
        if len(p) == 10:
            print(*p)
            p.clear()
    if p:
        print(*p)
