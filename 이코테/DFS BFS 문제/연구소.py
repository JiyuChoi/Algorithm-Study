from collections import deque
import copy
import sys
sys.setrecursionlimit(10000)

n, m = map(int, input().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d = deque()
res = 0

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def wall(s, l):
    if l == 3:
        virus()
        return
    else:
        for i in range(s, n*m):
            x = i // m
            y = i % m
            if not ground[x][y]:
                ground[x][y] = 1
                wall(i+1, l+1)
                ground[x][y] = 0

def virus():
    global res
    graph = copy.deepcopy(ground)
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                d.append((i,j))
    while d:
        x, y = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not graph[nx][ny]:
                d.append((nx, ny))
                graph[nx][ny] = 2

    cnt = 0
    for row in graph:
        cnt += row.count(0)
    if cnt > res:
        res = cnt

wall(0, 0)
print(res)