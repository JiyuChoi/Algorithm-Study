from collections import deque

n, m, v = map(int, input().split())
route = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x, y = map(int, input().split())
    route[x][y] = route[y][x] = 1

visited = [0]*(n+1)
d = deque()

# dfs 함수 정의
def dfs(l):
    visited[l] = 1
    print(l, end=" ")
    for i in range(1, n+1):
        if not visited[i] and route[l][i]:
            dfs(i)

# bfs 함수 정의
def bfs(l):
    # 시작점 추가 및 방문 처리
    d.append(l)
    visited[l] = 0
    while d:
        l = d.popleft()
        print(l, end=" ")
        for i in range(1, n+1):
            if visited[i] and route[l][i]:
                d.append(i)
                visited[i] = 0


dfs(v)
print()
bfs(v)


# 9/27
n, m, v = map(int, input().split())
route = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    route[a][b] = route[b][a] = 1

visited = [0]*(n+1)
def dfs(l):
    visited[l] = 1
    print(l, end=" ")
    for i in range(1, n+1):
        if not visited[i] and route[l][i]:
            dfs(i)

d = deque()
def bfs(l):
    d.append(l)
    visited[l] = 0
    while d:
        l = d.popleft()
        print(l, end=" ")
        for i in range(1, n+1):
            if visited[i] and route[l][i]:
                d.append(i)
                visited[i] = 0

dfs(v)
print()
bfs(v)