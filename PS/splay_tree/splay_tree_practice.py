class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.parent = None
        self.key = key
        self.cnt = 0


class SplayTree:
    def __init__(self):
        self.root = None

    def rotate(self, node):
        parent = node.parent
        if not parent:  # node가 루트노드면 종료
            return
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
                            (parent == parent.left) else node)
            self.rotate(node)

    def insert(self, key):
        node = self.root
        if not node:
            self.root = Node(key)
            return
        while True:
            if key == node.key:
                return
            elif key < node.key:
                if not node.left:
                    x = node.left = Node(key)
                    break
                else:
                    node = node.left
            else:
                if not node.right:
                    x = node.right = Node(key)
                    break
                else:
                    node = node.right
        x.parent = node
        self.splay(x)

    def find(self, key):
        node = self.root
        if not node:  # 트리가 비어있음
            return False
        while node:  # 탐색
            if key == node.key:  # 탐색 성공
                break
            elif key < node.key:  # 현재 노드보다 작으면 왼쪽으로
                if not node.left:  # 탐색 실패
                    break
                node = node.left
            else:  # 현재 노드보다 크면 오른쪽으로
                if not node.right:  # 탐색 실패
                    break
                node = node.right
        self.splay(node)  # 탐색한 마지막 정점을 루트로
        return key == node.key  # 찾았으면 true, 아니면 false

    def delete(self, key):
        if not self.find(key):  # 삭제할 노드를 splay
            return  # 못찾았으면 그만 두기
        node = self.root
        if node.left:
            if node.right:  # 자식 노드가 두 개 다 있을 때, 오른쪽 서브 트리를 왼쪽에 붙이기
                self.root = node.left  # 루트는 왼쪽 자식 노드가 되고
                self.root.parent = None  # 새로 생긴 루트는 부모가 없음
                x = self.root  # 왼쪽 서브트리의 가장 오른쪽 말단에
                while x.right:
                    x = x.right
                x.right = node.right  # 오른쪽 서브트리를 붙여주어야 함
                node.right.parent = x
                self.splay(x)  # x를 루트로 만들어줌
                del node  # 예전 루트노드 삭제
                return
            self.root = node.left  # 자식 노드가 왼쪽만 있을 때, 그냥 루트만 삭제해주면 됨
            self.root.parent = None
            del node
            return
        elif node.right:  # 자식 노드가 오른쪽만 있을 때, 루트만 삭제
            self.root = node.right
            self.root.parent = None
            del node
            return
        else:  # 둘 다 없으면 그냥 삭제
            del node
            self.root = None

    def update(self, node):
        node.cnt = 1
        if node.left:
            node.cnt += node.left.cnt
        if node.right:
            node.cnt += node.right.cnt

    def Find_Kth(self, k):
        node = self.root
        while True:
            while node.left and node.left.cnt > k:
                node = node.left
            if node.left:
                k -= node.left.cnt
            if not k:
                break
            k -= 1
            node = node.right
        self.splay(node)

    def find_max(self):
        node = self.root
        while node.right:
            node = node.right
        return node.key

    def find_min(self):
        node = self.root
        while node.left:
            node = node.left
        return node.key

    def lower_bound(self, key):
        node = self.root
        left, right = None, None
        while True:
            if key <= node.key:
                right = node
                if not node.left:
                    break
                node = node.left
            else:
                left = node
                if not node.right:
                    break
                node = node.right
        return right

    def upper_bound(self, key):
        node = self.root
        left, right = None, None
        while True:
            if key < node.key:
                right = node
                if not node.left:
                    break
                node = node.left
            else:
                left = node
                if not node.right:
                    break
                node = node.right
        return right


arr = [2, 3, 7, 4, 6, 3, 1, 5, 10]
tree = SplayTree()
for x in arr:
    tree.insert(x)

x = tree.lower_bound(7)
y = tree.upper_bound(7)
print(x.key)
print(y.key)
