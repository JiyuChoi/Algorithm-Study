# board = [list(map(int, input().split())) for _ in range(7)]
# cnt = 0
#
# for i in range(3):
#     for j in range(7):
#         tmp = board[j][i:i+5]
#         if tmp == tmp[::-1]:
#             cnt += 1
#         for k in range(2):
#             if board[i + k][j] != board[i + 5 - k - 1][j]:
#                 break
#         else:
#             cnt += 1
#
# print(cnt)
#
#
# for n in range(7):
#     for i in range(3):
#         row = col = []
#         for j in range(i, i+5):
#             row.append(board[n][j])
#             col.append(board[j][n])
#         if row == row[::-1]:
#             cnt += 1
#         if col == col[::-1]:
#             cnt += 1
#
# print(cnt)

board = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(7):
    for j in range(3):
        row, col = [], []
        for k in range(5): #for k in range(j, j+5):
            row.append(board[i][j+k]) #row.append(board[i][k])
            col.append(board[j+k][i]) #col.append(board[k][j])
        if row == row[::-1]:
            cnt += 1
        if col == col[::-1]:
            cnt += 1

print(cnt)
