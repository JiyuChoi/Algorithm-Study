# import sys
# # 재귀 한도 설정
# sys.setrecursionlimit(10**6)
#
# # 방향 벡터 설정
# dx = [1, 1, 1, 0, 0, -1, -1, -1]
# dy = [0, -1, 1, -1, 1, 0, -1, 1]
#
# def dfs(x, y):
#     ground[x][y] = 0
#     for i in range(8):
#         xx = x + dx[i]
#         yy = y + dy[i]
#         if 0<=xx<h and 0<=yy<w and ground[xx][yy]:
#             dfs(xx, yy)
#
# while True:
#     w, h = map(int, sys.stdin.readline().split())
#     # w, h 값이 0 이면 break
#     if not w and not h:
#         break
#     ground = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
#     cnt = 0
#
#     for i in range(h):
#         for j in range(w):
#             if ground[i][j]:
#                 cnt += 1
#                 dfs(i, j)
#     print(cnt)

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]
def dfs(x, y):
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<h and 0<=ny<w and board[nx][ny]:
            board[nx][ny] = 0
            dfs(nx, ny)

while True:
    w, h = map(int, input().split())
    if (w, h) == (0, 0):
        break
    board = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):
            if board[i][j] == 1:
                cnt += 1
                dfs(i, j)
    print(cnt)