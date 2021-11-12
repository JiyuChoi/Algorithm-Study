from collections import deque
import sys

N, L, R = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    united = []
    united.append((x, y))
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visit[nx][ny]:
                if L <= abs(graph[nx][ny] - graph[x][y]) <= R:
                    visit[nx][ny] = 1
                    q.append((nx, ny))
                    united.append((nx, ny))
    return united

res = 0
while True:
    visit = [[0]*N for _ in range(N)]
    is_move = False
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                visit[i][j] = 1
                united = bfs(i, j)
                if len(united) > 1:
                    is_move = True
                    num = sum([graph[x][y] for x, y in united]) // len(united)
                    for x, y in united:
                        graph[x][y] = num

    if not is_move:
        break
    res += 1
print(res)