# 제곱수인지 아닌지 판별 가능한 배열 (True, False)
# 제곱수끼리 모아둔 배열
# n이 제곱수면 1
# 1 - n -> i, n-i 제곱수면 2
# 1 - n -> 2개 i,j, n-i-j 가 제곱수면 3
# 4

def chk(n, is_sq, sq):
    if is_sq[n]:
        return 1
    m = len(sq)
    for i in range(m):
        if sq[i] > n:
            break
        if is_sq[n-sq[i]]:
            return 2
    for i in range(m):
        if sq[i] > n:
            break
        for j in range(i, m):
            if sq[i]+sq[j] > n:
                break
            if is_sq[n-sq[i]-sq[j]]:
                return 3
    return 4


is_sq = [False]*(50001)
sq = []
i = 1
while i*i <= 50000:
    is_sq[i*i] = True
    sq.append(i*i)
    i += 1
ans = [0]
for i in range(1, 50001):
    ans.append(chk(i, is_sq, sq))
print(ans)
