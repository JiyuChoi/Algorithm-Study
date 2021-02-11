import sys

# DFS 풀이

# n, m 값 입력 받기
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
link = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)
visited[1] = 1
cnt = 0

def dfs(x):
    global cnt
    visited[x] = 1
    for y in range(2, n+1):
        if link[x][y] and not visited[y]:
            cnt += 1
            dfs(y)

for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    link[x][y] = link[y][x] = 1

for i in range(2, n+1):
    if link[1][i] and not visited[i]:
        cnt += 1
        dfs(i)

print(cnt)



#BFS 풀이

from collections import deque

def bfs():
    global cnt
    while d:
        l = d.popleft()
        cnt += 1
        for i in range(1, n+1):
            if not visited[i] and link[l][i]:
                d.append(i)
                visited[i] = 1

# n, m 값 입력 받기
# n = int(input())
# m = int(input())
# link = [[0]*(n+1) for _ in range(n+1)]
#
# for _ in range(m):
#     x, y = map(int, input().split())
#     link[x][y] = link[y][x] = 1

visited = [0]*(n+1)
d = deque()
d.append(1)
visited[1] = 1
cnt = 0

bfs()
print(cnt-1)