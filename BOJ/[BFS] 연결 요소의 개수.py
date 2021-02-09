import sys
# 파이썬에서는 재귀 허용치가 넘어가면 에러남
# DFS에서 설정해줘야 런타임 에러가 안남
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
link = [[0]*(n+1) for _ in range(n+1)]
cnt = 0
visited = [0]*(n+1)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    link[x][y] = link[y][x] = 1

def dfs(i):
    visited[i] = 1
    for j in range(1,n+1):
        if link[i][j] == 1 and link[j][i] == 1 and visited[j] == 0:
            dfs(j)

for i in range(1,n+1):
    if visited[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)
