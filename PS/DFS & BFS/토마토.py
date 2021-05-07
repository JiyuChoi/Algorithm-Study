from collections import deque
n, m = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(m)]
dis = [[0]*n for _ in range(m)]
d = deque()

dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            d.append((i,j))

while d:
    x, y = d.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n and tomato[nx][ny]==0:
            d.append((nx, ny))
            tomato[nx][ny] = 1
            dis[nx][ny] = dis[x][y] + 1

flag = 1
for i in range(m):
    for j in range(n):
        if tomato[i][j] == 0:
            flag = 0
result = 0
if flag == 1:
    for i in range(m):
        for j in range(n):
            if dis[i][j] > result:
                result = dis[i][j]
    print(result)
else:
    print(-1)




