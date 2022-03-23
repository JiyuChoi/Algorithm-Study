# n = int(input())
# num = list(map(int, input().split()))
#
# dy = [1]*n
#
# for i in range(1, n):
#     for j in range(i):
#         if num[i] > num[j]:
#             dy[i] = max(dy[i], dy[j]+1)
#
# print(max(dy))

n = int(input())
num = list(map(int, input().split()))
dp = [1]*n

for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
