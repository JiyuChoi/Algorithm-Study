import sys
input = sys.stdin.readline

def rollin(i):
    if i == 0:
        dice[0], dice[3], dice[5], dice[2] = dice[3], dice[5], dice[2], dice[0]
    elif i == 1:
        dice[0], dice[3], dice[5], dice[2] = dice[2], dice[0], dice[3], dice[5]
    elif i == 2:
        dice[0], dice[1], dice[5], dice[4] = dice[4], dice[0], dice[1], dice[5]
    else:
        dice[0], dice[1], dice[5], dice[4] = dice[1], dice[5], dice[4], dice[0]

n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
move = list(map(int, input().split()))

dice = [0]*6

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for dir in move:
    i = dir-1
    nx = x + dx[i]
    ny = y + dy[i]
    if nx<0 or nx>=n or ny<0 or ny>=m:
        continue
    else:
        rollin(i)

    if board[nx][ny] == 0:
        board[nx][ny] = dice[5]
    else:
        dice[5] = board[nx][ny]
        board[nx][ny] = 0
    x, y = nx, ny
    print(dice[0])