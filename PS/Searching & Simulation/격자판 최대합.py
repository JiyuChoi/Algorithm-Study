n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = float("-inf")

for i in range(n):
    row_sum = col_sum = 0
    for j in range(n):
        row_sum += board[i][j]
        col_sum += board[j][i]
    max_sum = max(row_sum, col_sum)
    if max_sum > res:
        res = max_sum

line_sum_1 = line_sum_2 = 0
for i in range(n):
    line_sum_1 += board[i][i]
    line_sum_2 += board[i][-(i+1)] # j = n-j-1
    max_sum = max(line_sum_1, line_sum_2)
    if max_sum > res:
        res = max_sum

print(res)