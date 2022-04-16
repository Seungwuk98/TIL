class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.left = self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, val: int) -> None:
        node = Node(val)
        if not self.root:
            self.root = node
            return
        curr = self.root
        while True:
            if val <= curr.val:
                if not curr.left:
                    curr.left = node
                    return
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = node
                    return
                curr = curr.right

    def search(self, val: int) -> Node:
        if not self.root:
            return None
        curr = self.root
        while True:
            if val == curr.val:
                return curr
            if val < curr.val:
                if not curr.left:
                    return None
                curr = curr.left
            else:
                if not curr.right:
                    return None
                curr = curr.right

    def delete(self, val: int) -> None:
        if not self.root:
            return
        curr = self.root
        prev = None
        while True:
            if val == curr.val:
                break
            if val < curr.val:
                if not curr.left:
                    return
                prev = curr
                curr = curr.left
            else:
                if not curr.right:
                    return
                prev = curr
                curr = curr.right
        if not curr.left and not curr.right:
            if prev:
                if curr == prev.left:
                    prev.left = None
                else:
                    prev.right = None
            if curr == self.root:
                self.root = None
            del curr
        elif curr.left:
            nxt = curr.left
            prevnxt = nxt
            while nxt.right:
                prevnxt = nxt
                nxt = nxt.right
            prevnxt.right = None
            nxt.left = curr.left
            nxt.right = curr.right
            if prev:
                if curr == prev.left:
                    prev.left = nxt
                else:
                    prev.right = nxt
            if curr == self.root:
                self.root = nxt
            del curr
        else:
            nxt = curr.right
            prevnxt = nxt
            while nxt.left:
                prevnxt = nxt
                nxt = nxt.left
            prevnxt.left = None
            nxt.left = curr.left
            nxt.right = curr.right
            if prev:
                if curr == prev.left:
                    prev.left = nxt
                else:
                    prev.right = nxt
            if curr == self.root:
                self.root = nxt
            del curr


bst = BST()
bst.insert(1)
bst.insert(2)
print(bst.delete(2))
print(bst.root.val)
