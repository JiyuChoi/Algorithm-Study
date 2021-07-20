# def check(board):
#     for i in range(9):
#         row = col = [0] * 10
#         for j in range(9):
#             # row에서 확인
#             row[board[i][j]] = 1
#             # col에서 확인
#             col[board[j][i]] = 1
#         if sum(row) != 9 or sum(col) != 9:
#             return False
#     for i in range(3):
#         for j in range(3):
#             box = [0] * 10
#             for k in range(3):
#                 for l in range(3):
#                     # 3*3 안에서 확인
#                     box[board[i*3+k][j*3+l]] = 1
#             if sum(box) != 9:
#                 return False
#     return True
#
#
# board = [list(map(int, input().split())) for _ in range(9)]
# if check(board):
#     print("YES")
# else:
#     print("NO")


board = [list(map(int, input().split())) for _ in range(9)]

flag = True
for i in range(9):
    ch_row = [0] * 10
    ch_col = [0] * 10
    for j in range(9):
        ch_row[board[i][j]] += 1
        ch_col[board[j][i]] += 1
    if sum(ch_row) != 9 or sum(ch_col) != 9:
        flag = False
        break

for i in range(0, 9, 3):
    ch_box = [0] * 10
    for j in range(i, i+3):
        for k in range(i, i+3):
            ch_box[board[j][k]] += 1
    if sum(ch_box) != 9:
        flag = False
        break

if flag == False:
    print("NO")
else:
    print("YES")




