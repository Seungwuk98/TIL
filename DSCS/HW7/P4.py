from typing import List
from bisect import bisect_left


def P4(matrix: List[List[int]], target: int) -> tuple:
    ##### Write your Code Here #####
    def lowerbound(arr: list, find: int, key=lambda x: x) -> int:
        lo = 0
        hi = len(arr)
        while lo < hi:
            mid = lo + hi >> 1
            if key(arr[mid]) < find:
                lo = mid+1
            else:
                hi = mid
        return lo
    i = lowerbound(matrix, target, lambda x: x[0])
    if i >= len(matrix):
        return -1, -1
    if matrix[i][0] > target:
        i -= 1
        if i < 0:
            return -1, -1
    j = lowerbound(matrix[i], target)
    if matrix[i][j] == target:
        return i, j
    else:
        return -1, -1
    ##### End of your code #####
