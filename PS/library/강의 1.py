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


class SegmentTree:
    tree = Array(SIZE)

    def constructor():
        root = build(start, end, 1)

        root


INF = 1
A = 1

A in [-INF, INF]

tree = Array(SIZE, 0)


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


def operation(value):
    pass


def update(index, value, start, end, node):
    if start == end:
        tree[node] = operation(tree[node], value)
        return
    mid = (start + end)/2
    update(index, value, start, mid, node*2)
    update(index, value, mid+1, end, node*2+1)
    tree[node] = merge(tree[node*2], tree[node*2]+1)


IDENTITY = 10


def query(L, R, start, end, node):
    if end < L or R < start:
        return IDENTITY
    if L <= start and end <= R:
        return tree[node]
    mid = (start + end)/2
    return merge(query(L, R, start, mid, node*2),
                 query(L, R, mid+1, end, node*2+1))
