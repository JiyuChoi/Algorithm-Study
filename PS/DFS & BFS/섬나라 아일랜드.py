from collections import deque
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
d = deque()
cnt = 0

dx=[-1, -1, 0, 1, 1, 1, 0, -1]
dy=[0, 1, 1, 1, 0, -1, -1, -1]

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            d.append((i,j))
            board[i][j] = 0
            cnt += 1
            while d:
                x, y = d.popleft()
                for k in range(8):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<n and 0<=ny<n and board[nx][ny]:
                        d.append((nx, ny))
                        board[nx][ny] = 0

print(cnt)

