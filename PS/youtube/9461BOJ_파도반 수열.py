dp = [0, 1, 1, 1, 2, 2]
for _ in range(95):
    dp.append(dp[-1]+dp[-5])

for _ in range(int(input())):
    print(dp[int(input())])
