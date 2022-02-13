n = int(input())
board = [[0]*n for _ in range(n)]

k = int(input())
# 사과 위치
for _ in range(k):
    x, y = map(int, input().split())
    board[x-1][y-1] = 2

l = int(input())
switch = [list(input().split()) for _ in range(l)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def find(xx, yy, i):
    x, y = 0, 0
    board[x][y] = 1
    cnt, idx = 0, 0
    q = [(x,y)]
    while True:
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and board[nx][ny] != 1:
            if board[nx][ny] == 0:
                board[nx][ny] = 1
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
            if board[nx][ny] == 2:
                board[nx][ny] = 1
                q.append((nx, ny))
        else:
            cnt += 1
            break
        x, y = nx, ny
        cnt += 1
        if idx < l and cnt == int(switch[idx][0]):
            c = switch[idx][1]
            if c == 'D':
                i = (i+1) % 4
            elif c == 'L':
                i = (i-1) % 4
            idx += 1
    return cnt

print(find(0,0,0))

# 220213
