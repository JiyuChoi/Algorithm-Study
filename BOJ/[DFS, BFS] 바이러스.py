# import sys
#
# # DFS 풀이 (좀 더 간결하고 가독성 높은 방법)
#
# # n, m 값 입력 받기
# n = int(sys.stdin.readline())
# m = int(sys.stdin.readline())
# link = [[] for _ in range(n+1)]
# visited = [0]*(n+1)
# cnt = 0
#
# def dfs(v):
#     global cnt
#     visited[x] = 1
#     # x와 연결된 노드 반복
#     for i in link[v]:
#         if not visited[i]:
#             cnt += 1
#             dfs(i)
#
# # 인접행렬 대신 리스트로 연결된 노드 정보들만 저장
# for _ in range(m):
#     x, y = map(int, sys.stdin.readline().split())
#     link[x].append(y)
#     link[y].append(x)
#
# dfs(1)
# print(cnt)

from collections import deque
import sys
input = sys.stdin.readline

def bfs(v):
    cnt = 0
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        now = q.popleft()
        for next in network[now]:
            if not visited[next]:
                cnt += 1
                q.append(next)
                visited[next] = 1

    return cnt

n = int(input())
m = int(input())

network = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    network[x].append(y)
    network[y].append(x)

print(bfs(1))