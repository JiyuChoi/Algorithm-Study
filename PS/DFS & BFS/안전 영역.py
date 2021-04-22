from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
d = deque()
max_value = float("-inf")

dx = [0,1,0,-1]
dy = [1,0,-1,0]

for k in range(100):
    ch = [[0]*n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > k and ch[i][j] == 0:
                d.append((i,j))
                ch[i][j] = 1
                cnt += 1
                while d:
                    x, y = d.popleft()
                    for m in range(4):
                        nx = x + dx[m]
                        ny = y + dy[m]
                        if 0<=nx<n and 0<=ny<n and board[nx][ny] > k and ch[nx][ny] == 0:
                            d.append((nx, ny))
                            ch[nx][ny] = 1
    if cnt > max_value:
        max_value = cnt
print(max_value)

