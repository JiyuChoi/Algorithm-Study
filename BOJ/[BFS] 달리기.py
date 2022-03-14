from collections import deque

n, m, k = map(int, input().split())
graph = [list(input()) for _ in range(n)]

y1, x1, y2, x2 = map(int, input().split())
x1 -= 1; y1 -= 1; x2 -= 1; y2 -= 1
visited = [[float('inf')] * m for _ in range(n)]

q = deque()
q.append((x1, y1))
visited[y1][x1] = 0

while q:
    x, y = q.popleft()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        nd = 1
        while 0 <= nx < m and 0 <= ny < n and k >= nd and graph[ny][nx] == '.' and visited[ny][nx] > visited[y][x]:
            if visited[ny][nx] == float('inf'):
                q.append((nx, ny))
                visited[ny][nx] = visited[y][x] + 1
            nx += dx
            ny += dy
            nd += 1

if visited[y2][x2] == float('inf'):
    print(-1)
else:
    print(visited[y2][x2])