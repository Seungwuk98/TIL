n = (1 << 17) + 2050
tree = [0]*(1 << 19)


def build(arr: list, start: int = 1, end: int = n, node: int = 1) -> None:
    if start == end:
        tree[node] = arr[start-1]
        return
    mid = start + end >> 1
    build(arr, start, mid, node << 1)
    build(arr, mid+1, end, node << 1 | 1)
    tree[node] = tree[node << 1] + tree[node << 1 | 1]


def update(idx: int, plus: int, start: int = 1, end: int = n, node: int = 1) -> None:
    if start == end:
        tree[node] += plus
        return
    mid = start + end >> 1
    if idx <= mid:
        update(idx, plus, start, mid, node << 1)
    else:
        update(idx, plus, mid+1, end, node << 1 | 1)
    tree[node] = tree[node << 1] + tree[node << 1 | 1]


def query(l: int, r: int, start: int = 1, end: int = n, node: int = 1) -> int:
    if end < l or r < start:
        return 0
    if l <= start and end <= r:
        return tree[node]
    mid = start + end >> 1
    return query(l, r, start, mid, node << 1) + query(l, r, mid+1, end, node << 1 | 1)


arr = [*range(1, n+1)]
build(arr)
print(query(2, 5))      # 2+3+4+5
update(3, 2)            # 3 -> 5
print(query(2, 5))      # 2+5+4+5
