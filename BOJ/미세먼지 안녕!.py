from collections import deque

def bfs():

    while mess:
        cnt = 0
        x, y = mess.popleft()
        spread = a[x][y]//5
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and a[nx][ny] != -1:
                tmp[nx][ny] += spread
                cnt += 1
        tmp[x][y] += a[x][y] - (spread * cnt)

r, c, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]

cleaner = []
mess = deque()

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

tmp = [[0]*c for _ in range(r)]
for _ in range(t):
    for i in range(r):
        for j in range(c):
            if a[i][j] == -1:
                tmp[i][j] = -1
            elif a[i][j] != 0: # 한 번 돈 것을 다시 mess에 추가하는 로직으로 수정
                mess.append((i,j))




    bfs()
    for x in tmp:
        print(x)
    print()


