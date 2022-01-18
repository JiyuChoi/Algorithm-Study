# from collections import deque
# import sys
#
# def bfs(v):
#     q = deque()
#     q.append(v)
#     dis[v] = 0
#     cnt = 0
#
#     while q:
#         v = q.popleft()
#         if v == end:
#             return dis[v]
#
#         for e in link[v]:
#             if dis[e] == -1:
#                 q.append(e)
#                 dis[e] = dis[v] + 1
#
#     return -1
#
#
# n = int(sys.stdin.readline())
# start, end = map(int, sys.stdin.readline().split())
# T = int(sys.stdin.readline())
# link = [[] for _ in range(n+1)]
# dis = [-1] * (n+1)
#
# for _ in range(T):
#     x, y = map(int, input().split())
#     link[x].append(y)
#     link[y].append(x)
#
# print(bfs(start))

from collections import deque
import sys

input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append(v)
    dis[v] = 0
    while q:
        now = q.popleft()
        if now == y:
            return dis[y]
        for nx in link[now]:
            if dis[nx] == -1:
                dis[nx] = dis[now] + 1
                q.append(nx)
    return -1

n = int(input())
x, y = map(int, input().split())
m = int(input())

link = [[] for _ in range(n+1)]
dis = [-1]*(n+1)

for _ in range(m):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)

print(bfs(x))