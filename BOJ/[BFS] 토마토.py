# # 10/2 (위의 방법보다 시간이 적게 걸림!)
# from collections import deque
# import sys
#
# n, m = map(int, sys.stdin.readline().split())
# tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
# d = deque()
#
# for i in range(m):
#     for j in range(n):
#         if tomato[i][j] == 1:
#             d.append((i,j))
#
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
#
# days = -1
# while d:
#     days += 1
#     for _ in range(len(d)): #1인 것 모두 하루 지나면 주변의 것이 익음!
#         x, y = d.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<m and 0<=ny<n and tomato[nx][ny] == 0:
#                 tomato[nx][ny] = tomato[x][y] + 1
#                 d.append((nx, ny))
#
# for x in tomato:
#     if 0 in x:
#         print(-1)
#         exit()
# else:
#     print(days)

from collections import deque
import sys

dx = [1,0,-1,0]
dy = [0,1,0,-1]

n, m = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
q = deque()

for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            q.append((i, j, 0))

while q:
    x, y, cnt = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n and not tomato[nx][ny]:
            tomato[nx][ny] = 1
            q.append((nx, ny, cnt + 1))

for box in tomato:
    if 0 in box:
        print(-1)
        exit()
else:
    print(cnt)