from collections import deque
import sys

# def bfs():
#     global days
#     while d:
#         days += 1
#         for _ in range(len(d)):
#             z, x, y = d.popleft()
#             for i in range(6):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 nz = z + dz[i]
#                 if 0<=nx<n and 0<=ny<m and 0<=nz<h and tomato[nz][nx][ny] == 0:
#                     d.append((nz,nx,ny))
#                     tomato[nz][nx][ny] = 1
#
#
#
# m, n, h = map(int, sys.stdin.readline().split())
# tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]
#
# d = deque()
# days = -1
#
# dx = [1,-1,0,0,0,0]
# dy = [0,0,1,-1,0,0]
# dz = [0,0,0,0,1,-1]
#
# for i in range(h):
#     for j in range(n):
#         for k in range(m):
#             if tomato[i][j][k] == 1:
#                 d.append((i, j, k))
#
# bfs()
# for x in tomato:
#     for y in x:
#         if 0 in y:
#             print(-1)
#             exit()
# print(days)

input = sys.stdin.readline

dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

m, n, h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

q = deque()
for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                q.append((i, j, k, 0))

while q:
    z, x, y, cnt= q.popleft()
    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if 0<=nx<n and 0<=ny<m and 0<=nz<h and tomato[nz][nx][ny] == 0:
            q.append((nz, nx, ny, cnt + 1))
            tomato[nz][nx][ny] = 1

for t in tomato:
    for x in t:
        if 0 in x:
            print(-1)
            exit()
else:
    print(cnt)
