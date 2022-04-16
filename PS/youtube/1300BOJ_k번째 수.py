# 배열에서 k번째 수 x 이분 탐색의 후보
# und < k
# bel >= k
# x -> k번째 수
# 1 2 3 4
# 2 4 6 8
# 3 6 9 12
# 4 8 12 16

def count(x):
    und = bel = 0
    for i in range(1, n+1):
        if n*i < x:
            und += n
            bel += n
            continue
        y = x//i
        bel += y
        und += y if x % i else y-1
    return und, bel


n = int(input())
k = int(input())
lo = 0
hi = int(1e10)
while lo < hi:
    mid = (lo+hi)//2
    und, bel = count(mid)
    if bel < k:
        lo = mid+1
    elif und >= k:
        hi = mid-1
    else:
        lo = mid
        break
print(lo)
