from collections import deque

n, m, k = map(int, input().split())
graph = [list(input()) for _ in range(n)]

x1, y1, x2, y2 = map(int, input().split())
x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
visited = [[1004]*m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

queue = deque()
queue.append((x1, y1))
visited[x1][y1] = 0

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        nk = 1
        while 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == '.' and nk <= k and visited[nx][ny] > visited[x][y]:
            if visited[nx][ny] == 1004:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
            nx += dx[i]
            ny += dy[i]
            nk += 1

if visited[x2][y2] == 1004:
    print(-1)
else:
    print(visited[x2][y2])