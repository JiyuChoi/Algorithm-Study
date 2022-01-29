# import sys
# sys.setrecursionlimit(10000)
#
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
#
# def dfs(x, y, number):
#     if len(number) == 6:
#         res.add(number)
#         return
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<=nx<5 and 0<=ny<5:
#             dfs(nx, ny, number+board[nx][ny])
#
# board = [list(input().split()) for _ in range(5)]
# res = set()
#
# for i in range(5):
#     for j in range(5):
#         dfs(i, j, board[i][j])
#
# print(len(res))

import sys
sys.setrecursionlimit(10000)

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def dfs(x, y, l, num):
    if l == 6:
        res.add(num)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<5 and 0<=ny<5:
                dfs(nx, ny, l+1, num+board[nx][ny])
    return
board = [list(input().split()) for _ in range(5)]
res = set()

for i in range(5):
    for j in range(5):
        dfs(i, j, 1, board[i][j])

print(len(res))