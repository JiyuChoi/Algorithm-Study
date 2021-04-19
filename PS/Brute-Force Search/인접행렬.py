n, m = map(int, input().split())
board = [[0]*n for _ in range(n)]
for _ in range(m):
    x, y, c = map(int, input().split())
    board[x-1][y-1] = c

for r in board:
    print(*r)