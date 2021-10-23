for _ in range(int(input())):
    n, m = map(int, input().split())
    g = list(map(int, input().split()))

    dp = []
    for i in range(0, len(g), m):
        dp.append(g[i:i+m])

    for j in range(1, m):
        for i in range(n):
            if i == 0:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j-1]) + dp[i][j]
            elif i == n-1:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j-1]) + dp[i][j]
            else:
                dp[i][j] = max(dp[i][j-1], dp[i+1][j-1], dp[i-1][j-1]) + dp[i][j]

    res = float("-inf")
    for row in dp:
        res = max(res, row[m-1])
    print(res)