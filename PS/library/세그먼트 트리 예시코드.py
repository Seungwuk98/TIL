import sys
input = sys.stdin.readline


N, M, K = map(int, input().split())
tree = [0]*(N << 2)
arr = [int(input())for _ in range(N)]


def merge(left, right):
    return left + right


def build(start=1, end=N, node=1) -> None:
    if start == end:
        tree[node] = arr[start-1]
        return
    mid = start + end >> 1  # (start + (end - start)//2)
    build(start, mid, node << 1)  # node*2
    build(mid+1, end, node << 1 | 1)  # node*2+1
    tree[node] = merge(tree[node << 1], tree[node << 1 | 1])


def update(index, plus, start=1, end=N, node=1) -> None:
    if start == end:
        tree[node] = plus
        return
    mid = start + end >> 1  # (start + (end - start)//2)
    if index <= mid:
        update(index, plus, start, mid, node << 1)  # node*2
    else:
        update(index, plus, mid+1, end, node << 1 | 1)  # node*2+1
    tree[node] = merge(tree[node << 1], tree[node << 1 | 1])


def query(left, right, start=1, end=N, node=1) -> int:
    if end < left or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = start + end >> 1  # (start + (end - start)//2)
    return merge(query(left, right, start, mid, node << 1),
                 query(left, right, mid+1, end, node << 1 | 1))


build()

for _ in range(M+K):
    op, l, r = map(int, input().split())
    if op == 1:
        update(l, r)
    else:
        print(query(l, r))
