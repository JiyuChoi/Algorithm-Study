n = int(input())
ground = [list(map(int,input())) for _ in range(n)]
cnt = 0
res = []

dx = [1,0,-1,0]
dy = [0,-1,0,1]


def dfs(x,y):
    global cnt
    cnt += 1
    ground[x][y] = 0
    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<n and 0<=yy<n and ground[xx][yy] == 1:
            dfs(xx,yy)


for i in range(n):
    for j in range(n):
        if ground[i][j] == 1:
            cnt = 0
            dfs(i,j)
            res.append(cnt)

print(len(res))
res.sort()
for i in res:
    print(i)