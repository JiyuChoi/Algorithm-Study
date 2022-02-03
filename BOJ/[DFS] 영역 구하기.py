# import sys
# sys.setrecursionlimit(10000)
#
# # 방향 벡터 설정
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
#
# # dfs 함수 정의
# def dfs(x, y):
#     global cnt
#     grid[x][y] = 1
#     for i in range(4):
#         xx = x + dx[i]
#         yy = y + dy[i]
#         if 0<=xx<m and 0<=yy<n and not grid[xx][yy]:
#             cnt += 1
#             dfs(xx, yy)
#
# # m, n, k 입력 받기
# m, n, k = map(int, sys.stdin.readline().split())
# # 모눈 종이 이차원 배열 생성
# grid = [[0]*n for _ in range(m)]
# res = []
#
# # k번 반복
# for _ in range(k):
#     # 모눈종이 꼭짓점 입력 받기
#     x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
#     # 직사각형 부분 1로 표시
#     for i in range(y1, y2):
#         for j in range(x1, x2):
#             grid[i][j] = 1
#
# # (0,0)부터 순회
# for i in range(m):
#     for j in range(n):
#         if grid[i][j] == 0:
#             # 넓이 1부터 시작
#             cnt = 1
#             dfs(i,j)
#             res.append(cnt)
#
#
# print(len(res))
# # 오름차순으로 정리
# res.sort()
# print(*res)


# # 10/4 bfs 풀
# from collections import deque
# import sys
#
# def bfs(i, j):
#     global cnt
#     d.append((i, j))
#     board[i][j] = 1
#     while d:
#         x, y = d.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<m and 0<=ny<n and not board[nx][ny]:
#                 board[nx][ny] = 1
#                 cnt += 1
#                 d.append((nx, ny))
#
#
# m, n, k = map(int, sys.stdin.readline().split())
# board = [[0]*n for _ in range(m)]
# for _ in range(k):
#     x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
#     for x in range(y1, y2):
#         for y in range(x1, x2):
#             board[x][y] = 1
#
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
# d = deque()
# res = []
#
# for i in range(m):
#     for j in range(n):
#         if not board[i][j]:
#             cnt = 1
#             bfs(i, j)
#             res.append(cnt)
#
# print(len(res))
# print(*sorted(res))

import sys
sys.setrecursionlimit(10000)

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    global cnt
    board[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n and not board[nx][ny]:
            cnt += 1
            dfs(nx, ny)

m, n, k = map(int, input().split())
board = [[0]*n for _ in range(m)]
res = []

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(y1, y2):
        for y in range(x1, x2):
            board[x][y] = 1

for i in range(m):
    for j in range(n):
        if not board[i][j]:
            cnt = 1
            dfs(i, j)
            res.append(cnt)

print(len(res))
print(*sorted(res))