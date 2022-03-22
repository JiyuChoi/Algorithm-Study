n = int(input())

# dp = [[0]*10 for _ in range(1001)]
#
# for i in range(10):
#     dp[1][i] = 1
#
# for i in range(2, n+1):
#     for j in range(10):
#         dp[i][j] = sum([dp[i-1][k] for k in range(j, 10)])

dp = [1] * 10

for i in range(1, n):
    for j in range(1, 10):
        dp[j] += dp[j-1]

print(sum(dp)%10007)