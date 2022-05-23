from re import S


sum = 1
start = 1
end = 1
left = 1
right = 1
root = 1
arr = []
tree = []
SIZE = 1

HF = SIZE/2


def build():
    for i in [0, arr.length-1]:
        tree[HF+i] = arr[i]
    for i in [HF-1, 1]:
        tree[i] = tree[i*2] + tree[i*2+1]


def update(index, value):
    index = HF + index
    tree[index] += value
    while index != 1:
        index /= 2
        tree[index] = tree[index*2] + tree[index*2+1]


def querySum(L, R) -> int:
    L += HF
    R += HF
    result = 0
    while L <= R:
        if L % 2 == 1:
            result += tree[L]
            L += 1
        if R % 2 == 0:
            result += tree[R]
            R -= 1
        L /= 2
        R /= 2
    return result


def Array(a):
    pass


tree = Array(SIZE)

DEFAULT_LAZY = 1


class SegmentTree:
    tree = Array(SIZE)
    lazy = Array(SIZE, DEFAULT_LAZY)

    def constructor():
        root = build(start, end, 1)

        root


def processFromLazy():
    return


def mergeLazys(child, parent):
    return


def propagation(start: int, end: int, node: int) -> None:
    if lazy[node] == DEFAULT_LAZY:
        return
    tree[node] = processFromLazy(start, end, lazy[node])
    if start != end:
        mergeLazys(node*2, node)
        mergeLazys(node*2+1, node)
    lazy[node] = DEFAULT_LAZY


INF = 1
A = 1

A in [-INF, INF]

tree = Array(SIZE, 0)
lazy = Array(SIZE, 0)


class T:
    pass


def merge(left: T, right: T) -> T:
    #############################
    #         세부 구현         #
    #############################
    pass


def merge(left: int, right: int) -> int:
    return left + right


def build(start, end, node):
    if start == end:
        tree[node].set(arr[start])
        return
    mid = (start + end)/2
    build(start, mid, node*2)
    build(mid+1, end, node*2+1)
    tree[node] = merge(tree[node*2], tree[node*2+1])


def update(key, start, end, node):
    if start == end:
        tree[node] += 1
        return
    mid = start + (end - start)/2
    if key <= mid:
        update(key, start, mid, node*2)
    else:
        update(key, mid+1, end, node*2+1)
    tree[node] = tree[node*2] + tree[node*2+1]


def operation(value):
    pass


def update(value, left, right, start, end, node):
    propagation(start, end, node)
    if end < left or right < start:
        return
    if left <= start and end <= right:
        lazy[node] = value
        propagation(start, end, node)
        return
    mid = (start + end) / 2
    update(value, left, right, start, mid, node*2)
    update(value, left, right, mid+1, end, node*2+1)
    tree[node] = merge(tree[node*2], tree[node*2+1])


IDENTITY = 10


def query(left, right, start, end, node):
    propagation(start, end, node)
    if end < left or right < start:
        return IDENTITY
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end)/2
    return merge(query(left, right, start, mid, node*2),
                 query(left, right, mid+1, end, node*2+1))


N = 1

arr = []


fenwick = Array(N + 1)


def build(prefix: list) -> None:
    for i in [1, N]:
        fenwick[i] = prefix[i] - prefix[i-(i & -i)]


def query_1_to_R(R: int) -> int:
    ret = 0
    while R > 0:
        ret += fenwick[R]
        R -= R & -R
    return ret


def query_L_to_R(L: int, R: int) -> int:
    return query_1_to_R(R) - query_1_to_R(L-1)


def update(index: int, val: int) -> None:
    while index <= N:
        fenwick[index] += val
        index += index & -index
