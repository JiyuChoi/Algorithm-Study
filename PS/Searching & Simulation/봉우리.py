n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 테두리 0 설정하기
board.insert(0, [0]*n)
board.append([0]*n)
for row in board:
    row.insert(0, 0)
    row.append(0)

# 방향벡터
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        # 상하좌우보다 모두 크다면 카운트 +1 하기
        if all(board[i][j] > board[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)