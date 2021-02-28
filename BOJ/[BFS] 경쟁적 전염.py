from collections import deque

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
target_s, target_x, target_y = map(int, input().split())
virus = []

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            virus.append((graph[i][j], 0, i, j))

virus.sort()
d = deque(virus)


while d:
    v, s, x, y = d.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and not graph[nx][ny]:
            graph[nx][ny] = v
            d.append((v, s+1, nx, ny))

print(graph[target_x-1][target_y-1])






