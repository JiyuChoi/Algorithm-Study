from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    cnt = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not visited[nx][ny] and war[nx][ny] == war[x][y]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1

    return cnt

n, m = map(int, input().split())
war = [list(input()) for _ in range(m)]
visited = [[0] * n for i in range(m)]

my, enemy = 0, 0

q = deque()
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            q.append((i, j))
            visited[i][j] = 1
            if war[i][j] == "W":
                my += bfs()**2
            else:
                enemy += bfs()**2

print(my, enemy)