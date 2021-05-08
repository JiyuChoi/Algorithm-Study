def dfs(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<=6 and 0<=ny<=6 and board[nx][ny] == 0:
                board[nx][ny] = 1
                dfs(nx, ny)
                board[nx][ny] = 0

# 미로 입력 받기
board = [list(map(int, input().split())) for _ in range(7)]
# 방향 백터
dx = [0,1,0,-1]
dy = [1,0,-1,0]

cnt = 0
board[0][0] = 1
dfs(0, 0)
print(cnt)