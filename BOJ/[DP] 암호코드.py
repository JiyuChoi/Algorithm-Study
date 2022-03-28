n = [0] + list(map(int,input()))

l = len(n) - 1
dp = [0]*(l+1)
dp[0], dp[1] = 1, 1

if n[1] == 0: # 맨 앞 숫자가 0이면 만들 수 없음!
    print("0")
else:
    for i in range(2, l+1):
        if n[i] > 0:
            dp[i] += dp[i-1]

        temp = n[i-1] * 10 + n[i]
        if 10 <= temp <= 26:
            dp[i] += dp[i-2] # (dp[i-1]+dp[i-2])

    print(dp[l] % 1000000)