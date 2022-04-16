class Node:
    def __init__(self, x: int) -> None:
        self.val = x
        self.prev = None


class MyStack:
    def __init__(self) -> None:
        self.tail = Node(None)
        self.size = 0

    def push(self, val: int) -> None:
        self.size += 1
        node = Node(val)
        node.prev = self.tail.prev
        self.tail.prev = node

    def pop(self) -> int:
        if not self.size:
            return
        ret = self.tail.prev.val
        node = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        del node
        return ret

    def top(self) -> int:
        if not self.size:
            return None
        return self.tail.prev.val

    def get_size(self) -> int:
        return self.size

    def is_empty(self) -> bool:
        return not self.size


stack = MyStack()
for i in range(10):
    stack.push(i)

for i in range(10):
    print(stack.pop())
