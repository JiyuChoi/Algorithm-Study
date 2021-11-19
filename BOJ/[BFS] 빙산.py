from collections import deque

def bfs():
    melt = deque()
    while d:
        cnt = 0
        x, y = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    cnt += 1
                else:
                    d.append((nx, ny))
                    visited[nx][ny] = 1
        if cnt:
            melt.append((x, y, cnt))

    while melt:
        mx, my, m = melt.popleft()
        graph[mx][my] = max(graph[mx][my] - m, 0)



N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

d = deque()
year = 0

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

while True:
    k = 0
    visited = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if graph[i][j] != 0 and visited[i][j] == 0:
                k += 1
                visited[i][j] = 1
                d.append((i, j))
                bfs()

    if k == 0:
        year = 0
        break
    if k >= 2:
        break
    year += 1

print(year)
