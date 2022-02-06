import sys
# 재귀 한도 설정
sys.setrecursionlimit(10000)

# 방향 벡터 설정
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]


def DFS(x, y, c):
    visited[x][y] = 1
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0 <= xx < n and 0 <= yy < n and not visited[xx][yy] and grid[xx][yy] == c:
            DFS(xx, yy, c)


# n 값 입력 받기
n = int(sys.stdin.readline())
# 그리드 값 입력 받기
grid = [list(input()) for _ in range(n)]
color = ['R', 'G', 'B']
res = []
flag = 0

for _ in range(2):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for c in color:
        for i in range(n):
            for j in range(n):
                # 적록색약의 경우 빨간색을 초록색으로 변환
                if flag:
                    if grid[i][j] == 'R':
                        grid[i][j] = 'G'
                if not visited[i][j] and grid[i][j] == c:
                    cnt += 1
                    DFS(i, j, c)
    res.append(cnt)
    # 적록색으로 설정
    flag = 1

print(*res)


# BFS 풀이
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
board = [list(input()) for _ in range(n)]

visited = [[0]*n for _ in range(n)]
cnt_3 = 0

def bfs(x, y):
    visited[x][y] = 1
    q = deque([(x, y)])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[nx][ny] == board[x][y]:
                q.append((nx, ny))
                visited[nx][ny] = 1

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt_3 += 1
            bfs(i, j)

cnt_2 = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 'R':
            board[i][j] = 'G'

visited = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            cnt_2 += 1
            bfs(i, j)

print(cnt_3, cnt_2)