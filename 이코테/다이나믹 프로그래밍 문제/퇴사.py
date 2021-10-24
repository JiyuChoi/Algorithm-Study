n = int(input())
t = []
p = []
for _ in range(n):
    T, P = map(int, input().split())
    t.append(T)
    p.append(P)

dp = [0]*(n+1)
for i in range(n-1, -1, -1):
    time = t[i] + i
    if time <= n:
        dp[i] = max(dp[time]+p[i], dp[i])
print(max(dp))