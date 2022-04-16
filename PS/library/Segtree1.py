arr = [*range(1, 257)]  # 1부터 256


class Node:
    def __init__(self) -> None:
        self.sum = 0                    # 구간의 합
        self.left = self.right = None   # 왼쪽, 오른쪽 자식


class Segtree:
    def __init__(self) -> None:
        # 세그먼트 트리 [1, 256] 범위 생성자
        self.root = self.init()
        # 트리의 루트 생성

    def init(self, start: int = 1, end: int = 256) -> Node:
        # 노드 생성
        node = Node()
        if start == end:
            # 마지막 계층 도달. 노드의 값 등록
            # 현재 세그먼트 트리는 1-based index이고
            # arr는 0-based index이므로 start에 1을 빼줌
            node.sum = arr[start-1]
            return node
        mid = start + end >> 1
        # 왼쪽, 오른쪽 자식들을 생성하고
        node.left = self.init(start, mid)
        node.right = self.init(mid+1, end)
        # 완성 이후 구간의 합을 줍줍
        node.sum = node.left.sum + node.right.sum
        return node

    def update(self, node: Node, idx: int, plus: int, start: int = 1, end: int = 256) -> None:
        # 노드를 업데이트
        # idx : 업데이트 하고자 하는 값
        # plus : 더하고자 하는 값
        if start == end:
            # 마지막 계층 도달. 노드의 값 추가
            node.sum += plus
            return

        mid = start + end >> 1
        # idx가 mid보다 작거나 같으면 왼쪽으로 아니면 오른쪽으로
        if idx <= mid:
            self.update(node.left, idx, plus, start, mid)
        else:
            self.update(node.right, idx, plus, mid+1, end)
        # 자식들 업데이트 완료. 구간합 줍줍
        node.sum = node.left.sum + node.right.sum

    def query(self, node: Node, l: int, r: int, start: int = 1, end: int = 256) -> int:
        # 구간합 구하기
        # l : 구간의 왼쪽 값, r : 구간의 오른쪽 값
        if end < l or r < start:
            return 0
        if l <= start and end <= r:
            return node.sum
        mid = start + end >> 1
        return self.query(node.left, l, r, start, mid) + self.query(node.right, l, r, mid+1, end)


tree = Segtree()

print(tree.query(tree.root, 2, 5))          # 2+3+4+5
tree.update(tree.root, 3, 2)                # 3 -> 5
print(tree.query(tree.root, 2, 5))          # 2+5+4+5
