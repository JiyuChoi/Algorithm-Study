n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = float("-inf")

for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += board[i][j]
        sum2 += board[j][i]
    if sum1 > res:
        res = sum1
    if sum2 > res:
        res = sum2

sum1 = sum2 = 0
for i in range(n):
    sum1 += board[i][i]
    sum2 += board[i][-(i+1)]
    if sum1 > res:
        res = sum1
    if sum2 > res:
        res = sum2
print(res)