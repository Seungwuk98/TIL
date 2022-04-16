n, m = map(int, input().split())
tree = list(map(int, input().split()))
# mid -> 성공 -> 후보o -> lo = mid
# mid -> 실패 -> 후보x -> hi = mid-1
lo, hi = 0, int(1e9)*2
while lo < hi:
    mid = (lo+hi)//2+1
    s = sum([max(0, x-mid) for x in tree])
    if s >= m:
        lo = mid
    else:
        hi = mid-1
print(lo)
