n = int(input())
point = [list(map(int, input().split()))for _ in range(n)]


def compare(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    if y1 != y2:
        return y1 > y2
    else:
        return x1 > x2


def qsort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr.pop()
    left = [x for x in arr if compare(pivot, x)]
    right = [x for x in arr if not compare(pivot, x)]

    return qsort(left) + [pivot] + qsort(right)


for x in qsort(point):
    print(' '.join(map(str, x)))
