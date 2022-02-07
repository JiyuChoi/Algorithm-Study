# from collections import deque
# import sys
#
# def bfs(v, target):
#     cnt = 0
#     q = deque([[v, cnt]])
#     while q:
#         value = q.popleft()
#         v = value[0]
#         cnt = value[1]
#         if v == target:
#             return cnt
#
#         if not visited[p]:
#             cnt += 1
#             visited[p] = 1
#             for e in link[p]:
#                 if not visited[e]:
#                     q.append([e, cnt])
#     return -1
#
#
# n = int(sys.stdin.readline())
# p1, p2 = map(int, sys.stdin.readline().split())
# T = int(sys.stdin.readline())
# link = [[] for _ in range(n+1)]
# visited = [0] * (n+1)
#
# for _ in range(T):
#     x, y = map(int, input().split())
#     link[x].append(y)
#     link[y].append(x)
#
# print(bfs(p1, p2))


import sys
sys.setrecursionlimit(100000)

def dfs(a, b, cnt):
    if a == b:
        print(cnt)
        sys.exit(0) # 여기서 return을 하면 안됨 -1 출력됨 (아예 종료!)
    visited[a] = 1
    for nx in link[a]:
        if 0 < nx <= n and not visited[nx]:
            dfs(nx, b, cnt + 1)
    return -1

n = int(input())
a, b = map(int, input().split())
m = int(input())

link = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    link[x].append(y)
    link[y].append(x)

print(dfs(a, b, 0))