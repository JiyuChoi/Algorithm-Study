# from collections import deque
#
# n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
# cheese = []
# d = deque()
#
# dx = [0,1,0,-1]
# dy = [1,0,-1,0]
#
# def bfs(x,y):
#     # -1로 초기화한 visited 리스트 생성
#     visited = [[-1]*m for _ in range(n)]
#     visited[x][y] = 1
#     d.append((x, y))
#     cnt = 0
#     while d:
#         x, y = d.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 해당 노드가 board 내에 있고 2번이상 방문하지 않은 경우
#             if 0<=nx<n and 0<=ny<m and visited[nx][ny] != 1:
#                 # 치즈가 있는 부분(1)이면
#                 if board[nx][ny]:
#                     # 방문 횟수 1 증가
#                     visited[nx][ny] += 1
#                     # 만약 1이라면 치즈 녹은 것 표시하고 cnt+1
#                     if visited[nx][ny]:
#                         board[nx][ny] = 0
#                         cnt += 1
#                 # 치즈가 없는 부분이라면 방문 처리 후 큐에 추가
#                 else:
#                     visited[nx][ny] = 1
#                     d.append((nx, ny))
#     return cnt
#
# # 치즈가 다 녹기 위한 시간
# time = 0
# while True:
#     time += 1
#     res = bfs(0,0)
#     # 만약 치즈가 다 녹았다면 정지
#     if not res:
#         break
#
# print(time-1)

from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d = deque()
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 2
    d.append((x, y))
    cnt = 0
    while d:
        x, y = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] != 2:
                if cheese[nx][ny]:
                    visited[nx][ny] += 1
                    if visited[nx][ny] == 2:
                        cheese[nx][ny] = 0
                        cnt += 1
                else:
                    visited[nx][ny] = 2
                    d.append((nx, ny))
    return cnt

time = 0
while True:
    time += 1
    res = bfs(0, 0)
    if not res:
        break
print(time-1)

