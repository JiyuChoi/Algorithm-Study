from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cheese = []

dx = [0,1,0,-1]
dy = [1,0,-1,0]


def bfs(x,y):
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    d = deque()
    d.append((x,y))
    cnt = 0
    while d:
        x, y = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny] = 1
                if board[nx][ny]:
                    board[nx][ny] = 0
                    cnt += 1
                else:
                    d.append((nx,ny))
    cheese.append(cnt)
    return cnt

while True:
    res = bfs(0,0)
    if not res:
        break

print(len(cheese)-1)
print(cheese[-2])

# 10/4
from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split())
cheese = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
removed = []

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
d = deque()

def bfs(x, y):
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    d.append((x,y))
    cnt = 0
    while d:
        x, y = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if cheese[nx][ny] == 1:
                    cnt += 1
                    cheese[nx][ny] = 0
                else:
                    d.append((nx, ny))
    removed.append(cnt)
    return cnt

while True:
    res = bfs(0, 0)
    if not res:
        break

print(len(removed)-1)
print(removed[-2])
