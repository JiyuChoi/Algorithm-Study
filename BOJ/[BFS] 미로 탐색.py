import sys
from collections import deque

miro = []
d = deque()

# 방향벡터 설정
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# n, m 값 입력받기
n, m = map(int, sys.stdin.readline().split())

# miro 값 입력받기
for i in range(n):
    miro.append(list(map(int,input())))

d.append([0,0])
miro[0][0] = 0

# 이동한 칸 개수 입력
res = [[0]*m for _ in range(n)]

while d:
    now = d.popleft()
    for i in range(4):
        x = now[0] + dx[i]
        y = now[1] + dy[i]
        if 0 <= x < n and 0 <= y < m and miro[x][y] == 1:
            miro[x][y] = 0
            res[x][y] = res[now[0]][now[1]] + 1
            d.append([x, y])

else:
    print(res[n-1][m-1]+1)