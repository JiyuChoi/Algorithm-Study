from collections import deque
import copy

def bfs():
    while mess:
        x, y, s = mess.popleft()
        if s == t:
            return
        spread = a[x][y]//5
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and a[nx][ny] != -1:
                mess.append((nx, ny, s+1))
                tmp[nx][ny] += spread
                cnt += 1
        tmp[x][y] += a[x][y] - (spread * cnt)

        mess.append((x, y, s+1))
    for i in range(r):
        for j in range(c):
            a[i][j] += tmp[i][j]

r, c, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]

mess = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

tmp = [[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if a[i][j] == -1:
            tmp[i][j] = -1
        elif a[i][j] != 0: # 한 번 돈 것을 다시 mess에 추가하는 로직으로 수정
            mess.append((i, j, 0))

for _ in range(t):
    bfs()
    for x in tmp:
        print(x)
    print()


