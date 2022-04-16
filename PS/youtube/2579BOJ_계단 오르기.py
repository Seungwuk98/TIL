# -> 𝑑𝑝[0][𝑖]=𝑑𝑝[1][𝑖−1]+𝑎[𝑖]
# -> 𝑑𝑝[1][𝑖]=max⁡(𝑑𝑝[0][𝑖−2], 𝑑𝑝[1][𝑖−2])+𝑎[𝑖]
n = int(input())
a = [int(input())for _ in range(n)]
dp = [[0]*(n+1) for _ in range(2)]
dp[1][1] = a[0]
if n >= 2:
    dp[0][2] = a[0] + a[1]
    dp[1][2] = a[1]
for i in range(3, n+1):
    dp[0][i] = dp[1][i-1] + a[i-1]
    dp[1][i] = max(dp[0][i-2], dp[1][i-2]) + a[i-1]
print(max(dp[0][n], dp[1][n]))
