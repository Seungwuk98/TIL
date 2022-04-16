# 𝑑𝑝[𝑖]=min⁡(𝑑𝑝[𝑖−1], 𝑑𝑝[𝑖/2], 𝑑𝑝[𝑖/3])+1            if 2 | i and 3 |  𝑖
# 𝑑𝑝[𝑖]=min⁡(𝑑𝑝[𝑖−1]  , 𝑑𝑝[𝑖/2])+1                     if 2 | i and 3∤𝑖
# 𝑑𝑝[𝑖]=min⁡〖(𝑑𝑝[𝑖−1], 𝑑𝑝[𝑖/3])+1〗                      if 2∤i and 3 | I
# 𝑑𝑝[𝑖]=𝑑𝑝[𝑖−1]+1                                         if 2∤I and 3∤i

n = int(input())
dp = [0]*(n+1)
for i in range(2, n+1):
    dp[i] = dp[i-1]+1
    if not i % 2:
        dp[i] = min(dp[i], dp[i//2]+1)
    if not i % 3:
        dp[i] = min(dp[i], dp[i//3]+1)
print(dp[n])

# 백트래킹
# BFS
# 창의적
