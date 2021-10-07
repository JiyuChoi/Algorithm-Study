# 계단 오르기와 다른 점은 꼭 마시지 않아도 되므로 두 번 이상 마시지 않을 수도 있다!

n = int(input())
wine = [0] + [int(input()) for _ in range(n)]

dp = [0]*(n+1)
dp[1] = wine[1]

if n >= 2:
    dp[2] = max(wine[1] + wine[2], dp[0] + wine[2])
    for i in range(3, n+1):
        dp[i] = max(dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i], dp[i-1])
print(dp[-1])