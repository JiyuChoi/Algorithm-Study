import sys

# DFS 풀이 (좀 더 간결하고 가독성 높은 방법)

# n, m 값 입력 받기
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
computer = [[] for _ in range(n+1)]
visited = [0]*(n+1)
cnt = 0

def dfs(x):
    global cnt
    visited[x] = 1
    # x와 연결된 노드 반복
    for y in computer[x]:
        if not visited[y]:
            cnt += 1
            dfs(y)

# 인접행렬 대신 리스트로 연결된 노드 정보들만 저장
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    computer[x].append(y)
    computer[y].append(x)

dfs(1)
print(cnt)


# DFS 풀이

# # n, m 값 입력 받기
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# link = [[0]*(n+1) for _ in range(n+1)]
# visited = [0]*(n+1)
# visited[1] = 1
# cnt = 0
#
# def dfs(x):
#     global cnt
#     visited[x] = 1
#     for y in range(2, n+1):
#         if link[x][y] and not visited[y]:
#             cnt += 1
#             dfs(y)
#
# for _ in range(m):
#     x, y = map(int, sys.stdin.readline().split())
#     link[x][y] = link[y][x] = 1

# 이부분 필요 없음 (1부터 시작하니깐 dfs(1)로 해도 같은 결과
# for i in range(2, n+1):
#     if link[1][i] and not visited[i]:
#         cnt += 1
#         dfs(i)
#
# print(cnt)



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