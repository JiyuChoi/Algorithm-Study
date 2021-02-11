import sys
# 재귀 한도 설정
sys.setrecursionlimit(10**6)

# 방향 벡터 설정
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

# 높이가 h 이상인 것부터 탐색
def DFS(x, y, h):
    visited[x][y]=1
    for i in range(4):
        xx=x+dx[i]
        yy=y+dy[i]
        if 0<=xx<n and 0<=yy<n and visited[xx][yy]==0 and ground[xx][yy]>h:
            DFS(xx, yy, h)

# n 값 입력 받기
n = int(sys.stdin.readline())
# 지역의 높이 정보 입력 받기
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
res = 0

for h in range(100):
    cnt = 0
    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 높이가 h 이상이고 방문하지 않은 경우
            if not visited[i][j] and ground[i][j] > h:
                cnt += 1
                DFS(i, j, h)

    # 최대 안전영역 개수
    res = max(cnt, res)
    if cnt == 0:
        break

print(res)



