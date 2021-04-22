from collections import deque

n = int(input())
board = [list(map(int, input())) for _ in range(n)]

# deque 정의
d = deque()
# 결과값 리스트
res = []

# 방향벡터 정의
dx = [1,0,-1,0]
dy = [0,1,0,-1]

for i in range(n):
    for j in range(n):
        # 집이 있는 곳이라면 큐에 추가
        if board[i][j] == 1:
            board[i][j] = 0
            d.append((i,j))
            # 단지수 1부터 카운트
            cnt = 1
            # bfs 수행
            while d:
                x, y = d.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<n and 0<=ny<n and board[nx][ny]:
                        cnt += 1
                        board[nx][ny] = 0
                        d.append((nx, ny))
            res.append(cnt)


print(len(res))
for x in sorted(res):
    print(x)