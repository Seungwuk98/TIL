# ππ[π]=ππ[πβ1]+2ππ[πβ2]
# νΌλ³΄λμΉ μμ΄ nλ²μ§Έ μμ κ΅¬νκΈ°
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
