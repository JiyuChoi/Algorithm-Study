n = int(input())
score = [int(input()) for _ in range(n)]
dy = [0]*n

# if n == 1:
#     print(score[0])
# else:
#     dy[0] = score[0]
#     dy[1] = score[0] + score[1]
#     for i in range(2, n):
#         dy[i] = max(dy[i-3]+score[i-1]+score[i], dy[i-2]+score[i])
#     print(dy[-1])

if n == 1:
    print(score[0])
else:
    dy[0] = score[0]
    dy[1] = score[0] + score[1]
    for i in range(2, n):
        dy[i] = max(dy[i-3]+score[i]+score[i-1], dy[i-2]+score[i]) # 무조건 마지막 계단을 올라야하므로 dp[i-1]은 해당되지 않는다.
    print(dy[-1])