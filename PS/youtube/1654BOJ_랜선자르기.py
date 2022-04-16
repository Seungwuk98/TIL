k, n = map(int, input().split())
lan = [int(input())for _ in range(k)]
# m의 길이 -> n개 성공 -> 후보, lo = m
# 실패 hi = m-1
lo = 1
hi = max(lan)
while lo < hi:
    mid = (lo+hi)//2+1
    s = sum([x//mid for x in lan])
    if s >= n:
        lo = mid
    else:
        hi = mid-1
print(lo)
