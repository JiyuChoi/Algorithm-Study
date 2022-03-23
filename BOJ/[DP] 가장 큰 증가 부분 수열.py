n = int(input())
num = list(map(int, input().split()))

dp = num[:] # dp = [0]*n 으로 하면 9번째생 줄 첫번째 비교에서 오류 발생

for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], num[i]+dp[j])

print(max(dp))