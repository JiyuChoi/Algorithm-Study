from collections import deque

# n 입력 받기
n = int(input())

# 지도 입력 받기
ground = [list(map(int,input())) for _ in range(n)]
cnt = 0
res = []

# 뱡향벡터 리스트
dx = [1,0,-1,0]
dy = [0,-1,0,1]

# DFS 풀이
def dfs(x,y):
    global cnt
    cnt += 1
    ground[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and ground[xx][yy] == 1:
            dfs(xx,yy)

# BFS 풀이
def bfs(i,j):
    global cnt
    d = deque()
    d.append((i,j))
    ground[i][j] = 0

    while d:
        cnt += 1
        now = d.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if 0<=x<n and 0<=y<n and ground[x][y] == 1:
                d.append((x,y))
                ground[x][y] = 0
    res.append(cnt)


# 모든 정점을 시작점으로 탐색
for i in range(n):
    for j in range(n):
        if ground[i][j] == 1:
            cnt = 0
            dfs(i,j)
            # bfs(i, j)
            res.append(cnt)


# 단지수 출력
print(len(res))

# 각 단지내 집의 수 (오름차순)
res.sort()
for i in res:
    print(i)


# 9/27
# bfs 풀이
from collections import deque

n = int(input())
board = [list(map(int, input())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

d = deque()
res = []

# dfs 풀이
def dfs(x, y):
    global cnt
    cnt += 1
    board[x][y] = 0
    for k in range(4):
         nx = x + dx[k]
         ny = y + dy[k]
         if 0<=nx<n and 0<=ny<n and board[nx][ny]:
             dfs(nx, ny)

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            # d.append((i, j))
            board[i][j] = 0
            cnt = 0
            dfs(i,j)
            res.append(cnt)
            # while d:
            #     cnt += 1
            #     x, y = d.popleft()
            #     for k in range(4):
            #         nx = x + dx[k]
            #         ny = y + dy[k]
            #         if 0<=nx<n and 0<=ny<n and board[nx][ny]:
            #             board[nx][ny] = 0
            #             d.append((nx, ny))
            # res.append(cnt)

print(len(res))
for x in sorted(res):
    print(x)