import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
dis = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    d = deque([(0, 0, 0)])
    dis[0][0][0] = 1
    while d:
        x, y, w = d.popleft()
        if x == n-1 and y == m-1:
            return dis[x][y][w]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not dis[nx][ny][w]:
                if not graph[nx][ny]:
                    d.append((nx, ny, w))
                    dis[nx][ny][w] = dis[x][y][w] + 1
                if w == 0 and graph[nx][ny]:
                    d.append((nx, ny, 1))
                    dis[nx][ny][1] = dis[x][y][w] + 1
    return -1

print(bfs())
