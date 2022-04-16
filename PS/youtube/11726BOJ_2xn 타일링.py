# 𝑑𝑝[𝑖]=𝑑𝑝[𝑖−1]+2𝑑𝑝[𝑖−2]
# 피보나치 수열 n번째 원소 구하기
# dp[1] = 1
# dp[2] = 3
D = 10007


def f(n):
    if n == 1:
        return 1
    if n == 2:
        return 3
    a, b = 1, 3  # dp[1], dp[2], a,b = b,a+b
    for i in range(n-2):
        a, b = b, (2*a+b) % D
    return b


print(f(int(input())))
