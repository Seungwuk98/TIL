n = (1 << 17) + 2050
tree = [0] * (1 << 19)
HALF = 1 << 18


def build(arr: list) -> None:
    for i in range(n):
        tree[i+HALF] = arr[i]
    for i in range(HALF-1, 0, -1):
        tree[i] = tree[i << 1] + tree[i << 1 | 1]


def update(idx: int, plus: int) -> None:
    idx += HALF
    tree[idx] += plus
    while idx >> 1:
        tree[idx >> 1] = tree[idx] + tree[idx ^ 1]
        idx >>= 1


def query(L: int, R: int) -> int:
    L += HALF
    R += HALF
    ret = 0
    while L <= R:
        if L & 1:
            ret += tree[L]
            L += 1
        if ~R & 1:
            ret += tree[R]
            R -= 1
        L >>= 1
        R >>= 1
    return ret


arr = [*range(1, n+1)]
build(arr)
print(query(1, 4))      # 2+3+4+5
update(1, 3)            # 3->6
print(query(1, 4))      # 2+6+4+5
