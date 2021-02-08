from collections import deque
import sys

# m, n 값 입력 받기
m, n = map(int, sys.stdin.readline().split())

# 창고 입력 받기
stock = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 날짜 체크 배열
days = [[0]*m for _ in range(n)]
d = deque()

# 방향벡터 설정
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    for j in range(m):
        # 익은 토마토라면 deque에 추가
        if stock[i][j] == 1:
           d.append((i,j))

while d:
   now = d.popleft()
   for k in range(4):
       x = now[0] + dx[k]
       y = now[1] + dy[k]
       if 0<=x<n and 0<=y<m and stock[x][y] == 0:
           stock[x][y] = 1
           d.append((x, y))
           days[x][y] = days[now[0]][now[1]] + 1


flag = 1
for i in range(n):
    for j in range(m):
        # 토마토가 모두 익어있는 상태
        if stock[i][j] == 0:
            flag = 0

result = 0
# 최소날짜 찾기
if flag ==1:
    for i in range(n):
        for j in range(m):
            if days[i][j] > result:
                result = days[i][j]
    print(result)

# 토마토가 모두 익지 못하는 상황
else:
    print(-1)