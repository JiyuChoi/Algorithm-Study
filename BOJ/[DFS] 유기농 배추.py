# import sys
# # 재귀 한도 설정
# sys.setrecursionlimit(10000)
#
# # 방향 벡터 설정
# dx = [1, 0, -1, 0]
# dy = [0, -1, 0, 1]
#
# def dfs(x,y):
#     ground[x][y] = 0
#     # 인접한 배추 확인
#     for i in range(4):
#         xx = x + dx[i]
#         yy = y + dy[i]
#         if 0<=xx<n and 0<=yy<m and ground[xx][yy] == 1:
#             dfs(xx,yy)
#
#
# T = int(input())
# for _ in range(T):
#     n, m, k = map(int, input().split())
#     ground = [[0]*m for _ in range(n)]
#     cnt = 0
#
#     # 배추 위치 입력
#     for _ in range(k):
#         x, y = map(int, input().split())
#         ground[x][y] = 1
#
#     # 배추 확인
#     for i in range(n):
#         for j in range(m):
#             if ground[i][j] == 1:
#                 dfs(i, j)
#                 cnt += 1
#
#     print(cnt)

import sys
sys.setrecursionlimit(100000)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    board[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n and board[nx][ny]:
            dfs(nx, ny)
    return

for _ in range(int(input())):
    m, n, k = map(int, input().split())
    board = [[0] * n for _ in range(m)]
    cnt = 0

    for _ in range(k):
        x, y = map(int, input().split())
        board[x][y] = 1

    for i in range(m):
        for j in range(n):
            if board[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)