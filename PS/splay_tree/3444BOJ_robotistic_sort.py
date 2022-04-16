import sys
input = sys.stdin.readline
print = sys.stdout.write


class Node:
    def __init__(self) -> None:
        self.left = None
        self.right = None
        self.parent = None
        self.val = 0
        self.cnt = 0
        self.inv = False


class SplayTree:
    def __init__(self):
        self.root = None
        self.dummyL = None
        self.dummyR = None

    def init(self, n):
        if self.root:
            del self.root
        self.root = self.dummyL = Node()
        pre = self.dummyL
        pre.cnt = n+2
        while n:
            node = Node()
            node.parent = pre
            pre.right = node
            node.cnt = n+1
            pre = node
            n -= 1
        self.dummyR = Node()
        self.dummyR.parent = pre
        pre.right = self.dummyR
        self.dummyR.cnt = 1

    def rotate(self, node):
        parent = node.parent
        if not parent:  # node가 루트노드면 종료
            return
        self.prop(parent)
        self.prop(node)
        if parent.left == node:  # node가 parent의 왼쪽 자식이면
            parent.left = x = node.right  # p의 왼쪽 자식에 노드의 오른쪽 자식을 넣고
            node.right = parent  # 노드의 오른쪽 자식이 p가 됨
        else:
            parent.right = x = node.left  # p의 오른쪽 자식에 노드의 왼쪽 자식을 넣고
            node.left = parent  # 노드의 왼쪽 자식이 p가 됨
        node.parent = parent.parent  # 노드의 부모는 p의 부모인 g가 되고
        parent.parent = node  # p의 부모는 노드가 됨
        if x:
            x.parent = parent  # 옮겨진 노드의 자식이 있다면, 그의 부모는 p가 됨
        if not node.parent:  # 만약 노드의 부모가 없다면 스스로 루트가 되고
            self.root = node
        elif node.parent.left == parent:  # 만약 g의 왼쪽 자식이 p였다면 노드가 g의 왼쪽자식이 되고
            node.parent.left = node
        else:  # 그 외에 경우에는 노드가 오른쪽 자식이 된다.
            node.parent.right = node
        self.update(parent)
        self.update(node)

    def splay(self, node):
        while node.parent:
            parent = node.parent
            grand = parent.parent
            if grand:
                self.rotate(parent if (node == parent.left) ==
                            (parent == grand.left) else node)
            self.rotate(node)

    def flip(self, l, r):
        self.interval(l, r)
        self.root.inv = not self.root.inv
        self.prop(self.root)

    def prop(self, node):
        if not node.inv:
            return
        node.left, node.right = node.right, node.left
        if node.left:
            node.left.inv = not node.left.inv
        if node.right:
            node.right.inv = not node.right.inv
        node.inv = False

    def interval(self, l, r):
        self.kth(l-1)
        tmp = self.root
        tmp.right.parent = None
        self.root = tmp.right
        self.kth(r-l+1)
        tmp.right = self.root
        self.root.parent = tmp
        self.root = tmp

    def add(self, i, x):
        self.kth(i)
        self.root.val += x

    def update(self, node):
        node.cnt = 1
        if node.left:
            node.cnt += node.left.cnt
        if node.right:
            node.cnt += node.right.cnt

    def kth(self, k):
        node = self.root
        self.prop(node)
        while True:
            while node.left and node.left.cnt > k:
                node = node.left
                self.prop(node)
            if node.left:
                k -= node.left.cnt
            if not k:
                break
            k -= 1
            node = node.right
            self.prop(node)
        self.splay(node)


tree = SplayTree()
while True:
    n = int(input())
    if not n:
        break
    tree.init(n)
    arr = [*map(int, input().split())]
    ptr = [[]for _ in range(n+1)]
    for i in range(1, n+1):
        tree.add(i, arr[i-1])
        ptr[arr[i-1]].append(tree.root)
    count = 1
    for v in ptr:
        if v:
            for w in v:
                tree.splay(w)
                k = tree.root.left.cnt
                print(str(k) + ' ')
                tree.flip(count, k)
                count += 1
    print('\n')
