# t = int(input())
#
# dy = [0]*101
# dy[1:11] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
#
# # n의 최대가 100이니 dy를 한번에 계산하고 답 출력
# for i in range(11, 101):
#     dy[i] = dy[i-1] + dy[i-5]
#
# for _ in range(t):
#     n = int(input())
#     print(dy[n])

dp = [0]*101
dp[1:11] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for i in range(11, 101):
    dp[i] = dp[i-1] + dp[i-5]

for _ in range(int(input())):
    n = int(input())
    print(dp[n])