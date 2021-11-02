import sys

n = int(input())
cards = [0] + list(map(int, sys.stdin.readline().split()))
dp = [0]*(n+1)

for i in range(1, n+1):
    for k in range(1, i+1):
        dp[i] = max(dp[i], cards[k] + dp[i-k])

print(dp[i])

