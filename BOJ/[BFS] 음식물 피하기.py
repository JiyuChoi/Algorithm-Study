from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def dfs(x, y):
    cnt = 1
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 2 and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = 1
                    cnt += 1
    return cnt

n, m, k = map(int, input().split())
graph = [[0]*m for _ in range(n)]
visited = [[0]*m for _ in range(n)]
ans = []

for _ in range(k):
    i, j = map(int, input().split())
    graph[i-1][j-1] = 2

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2 and not visited[i][j]:
            res = dfs(i, j)
            ans.append(res)

print(max(ans))