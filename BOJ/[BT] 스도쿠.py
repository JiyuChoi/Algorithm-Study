import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zero = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

# 스도쿠에 없는 값 확인 (row, col, box)
def number(i, j):
    arr = [n+1 for n in range(9)]
    for k in range(9):
        if board[i][k] in arr:
            arr.remove(board[i][k])
        if board[k][j] in arr:
            arr.remove(board[k][j])

    i = (i//3) * 3
    j = (j//3) * 3
    for x in range(i, i+3):
        for y in range(j, j+3):
            if board[x][y] in arr:
                arr.remove(board[x][y])
    return arr

def dfs(l):
    if l == len(zero):
        for row in board:
            print(*row)
        sys.exit()

    (i, j) = zero[l]
    for num in number(i, j):
        board[i][j] = num
        dfs(l+1)
        board[i][j] = 0

dfs(0)