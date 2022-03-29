# n = int(input())
# price = [0] + list(map(int, input().split()))
# dp = [0]*(n+1)
#
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         dp[i] = max(dp[i], dp[i-j] + price[j])
#
# print(dp[-1])

n = int(input())
cost = [0] + list(map(int, input().split()))
dp = [0]*(n+1)

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], dp[i-j] + cost[j]) # for j 돌아가는 값에서 비교!

print(dp[-1])