def dfs(x, y):
    global cnt
    if x == max_x and y == max_y:
        cnt += 1
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and board[nx][ny] > board[x][y] and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                dfs(nx, ny)
                visited[nx][ny] = 0

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
min_v = float("inf")
max_v = float("-inf")

for i in range(n):
    for j in range(n):
        if board[i][j] < min_v:
            min_v = board[i][j]
            min_x, min_y = i, j
        if board[i][j] > max_v:
            max_v = board[i][j]
            max_x, max_y = i, j

dx = [1,0,-1,0]
dy = [0,1,0,-1]
cnt = 0
visited[min_x][min_y] = 1
dfs(min_x, min_y)
print(cnt)