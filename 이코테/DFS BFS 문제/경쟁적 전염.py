from collections import deque

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

d = deque()
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            d.append((i, j, board[i][j], 0))

while d:
    i, j, m, s_target = d.popleft()
    # s초 뒤에 출력하는 조건문
    if s == s_target:
        break
    for l in range(4):
        nx = i + dx[l]
        ny = j + dy[l]
        if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
            board[nx][ny] = m
            d.append((nx, ny, m, s_target+1))

print(board[x-1][y-1])


