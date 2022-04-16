n = (1 << 17) + 2050


class Node:
    def __init__(self) -> None:
        self.sum = 0
        self.lazy = 0  # 징표


tree = [Node()for _ in range(1 << 19)]


def build(arr: list, start: int = 1, end: int = n, node: int = 1) -> None:
    if start == end:
        tree[node].sum = arr[start-1]
        return
    mid = start + end >> 1
    build(arr, start, mid, node << 1)
    build(arr, mid+1, end, node << 1 | 1)
    tree[node].sum = tree[node << 1].sum + tree[node << 1 | 1].sum


def propagation(node: int, start: int, end: int) -> None:
    if not tree[node].lazy:
        return
    tree[node].sum += (end - start + 1) * tree[node].lazy
    if (start ^ end):  # start != end와 동일한 역할의 비트연산
        # start != end라는 뜻은 자식 노드가 존재한다는 뜻.
        tree[node << 1].lazy += tree[node].lazy
        tree[node << 1 | 1].lazy += tree[node].lazy
    # 전파 이후에는 징표 삭제
    tree[node].lazy = 0


def update_point(idx: int, plus: int, start: int = 1, end: int = n, node: int = 1) -> None:
    propagation(node, start, end)
    if start == end:
        tree[node].sum += plus
        return
    mid = start + end >> 1
    if idx <= mid:
        update_point(idx, plus, start, mid, node << 1)
    else:
        update_point(idx, plus, mid+1, end, node << 1 | 1)
    tree[node].sum = tree[node << 1].sum + tree[node << 1 | 1].sum


def update_range(plus: int, l: int, r: int, start: int = 1, end: int = n, node: int = 1) -> None:
    propagation(node, start, end)
    if end < l or r < start:
        return
    if l <= start and end <= r:
        tree[node].lazy += plus
        propagation(node, start, end)
        return
    mid = start + end >> 1
    update_range(plus, l, r, start, mid, node << 1)
    update_range(plus, l, r, mid+1, end, node << 1 | 1)
    tree[node].sum = tree[node << 1].sum + tree[node << 1 | 1].sum


def query(l: int, r: int, start: int = 1, end: int = n, node: int = 1) -> int:
    if end < l or r < start:
        return 0
    if l <= start and end <= r:
        return tree[node].sum
    mid = start + end >> 1
    return query(l, r, start, mid, node << 1) + query(l, r, mid+1, end, node << 1 | 1)


arr = [*range(1, n+1)]
build(arr)
print(query(2, 5))      # 2+3+4+5
update_range(4, 2, 3)     # 2 -> 6, 3 -> 7
print(query(2, 5))      # 6+7+4+5
