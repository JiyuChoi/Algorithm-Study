import sys
# 재귀 한도 설정
sys.setrecursionlimit(10**6)

# 방향 벡터 설정
dx = [1, 1, 1, 0, 0, -1, -1, -1]
dy = [0, -1, 1, -1, 1, 0, -1, 1]

def dfs(x, y):
    ground[x][y] = 0
    for i in range(8):
        xx = x + dx[i]
        yy = y + dy[i]
        if 0<=xx<h and 0<=yy<w and ground[xx][yy]:
            dfs(xx, yy)

while True:
    w, h = map(int, sys.stdin.readline().split())
    # w, h 값이 0 이면 break
    if not w and not h:
        break
    ground = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if ground[i][j]:
                cnt += 1
                dfs(i, j)
    print(cnt)