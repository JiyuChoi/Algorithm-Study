n = int(input())
num = list(map(int, input().split()))
dp = [0]*n
for i in range(n):
    dp[i] = max(dp[i-1] + num[i], num[i]) #그 전까지 (합한 값+ 더할 값)과 현재 더할 값을 비교해 큰 값을 넣기
    # if dp[i-1] + num[i] > num[i]:
    #     dp[i] = dp[i-1] + num[i]
    # else:
    #     dp[i] = num[i]
print(max(dp))