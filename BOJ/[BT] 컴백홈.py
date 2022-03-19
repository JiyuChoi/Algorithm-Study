import sys
input=sys.stdin.readline

def dfs(x, y, dis):
    global answer
    if dis > k:
        return
    if dis == k and x == 0 and y == c-1:
        answer += 1
        return

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<r and 0<=ny<c and not visited[nx][ny] and board[nx][ny] == ".":
            visited[nx][ny] = 1
            dfs(nx, ny, dis + 1)
            visited[nx][ny] = 0

r, c, k = map(int, input().split())
board = [input() for _ in range(r)]
visited = [[0]*c for _ in range(r)]
visited[r-1][0] = 1

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 0

dfs(r-1, 0, 1)
print(answer)