# fibonacci(n) -> dp[0][n], dp[1][n]
# fibonacci(n) -> fibo(n-1), fibo(n-2)
# dp[0][n] = dp[0][n-1] + dp[0][n-2] -> 피보나치
# dp[1][n] = dp[1][n-1] + dp[1][n-2]
# dp[0][0] = 1, dp[0][1] = 0
# dp[1][0] = 0, dp[1][1] = 1


def fibonacci(n):
    if n == 0:
        print(0)
        return 0
    if n == 1:
        print(1)
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


dp = [[0]*(41) for _ in range(2)]
dp[0][0] = dp[1][1] = 1
dp[0][1] = dp[1][0] = 0
for i in range(2, 41):
    dp[0][i] = dp[0][i-1] + dp[0][i-2]
    dp[1][i] = dp[1][i-1] + dp[1][i-2]

for _ in range(int(input())):
    n = int(input())
    print(dp[0][n], dp[1][n])
