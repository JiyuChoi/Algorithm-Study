from collections import deque

# 격자판 정보 입력
board = [list(map(int, input().split())) for _ in range(7)]

# 방향 벡터
dx = [1,0,-1,0]
dy = [0,1,0,-1]

d = deque()

# 처음 출발지 큐에 추가
d.append((0,0))
board[0][0] = 1

# dfs 함수 수행
while d:
    x, y = d.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<7 and 0<=ny<7 and board[nx][ny] == 0:
            d.append((nx, ny))
            board[nx][ny] = board[x][y] + 1

# 만약 도착점이 0이라면 (끝까지 가지 못한 경우)
if board[6][6] == 0:
    print(-1)
# 도착점이 0이 아니라면 (끝까지 간 경우)
else:
    print(board[6][6] - 1)