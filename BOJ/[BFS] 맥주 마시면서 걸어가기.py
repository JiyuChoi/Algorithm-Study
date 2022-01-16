# from collections import deque
#
# def bfs():
#     while d:
#         x, y = d.popleft()
#         if abs(festa[0]-x) + abs(festa[1]-y) <= 1000:
#             return True
#         for i in range(n):
#             nx, ny = con[i]
#             if abs(nx-x) + abs(ny-y) <= 1000 and not visited[i]:
#                 visited[i] = 1
#                 d.append((nx, ny))
#     return False
#
# for _ in range(int(input())):
#     n = int(input())
#     home = list(map(int, input().split()))
#     con = [list(map(int, input().split())) for _ in range(n)]
#     festa = list(map(int, input().split()))
#
#     visited = [0]*n
#     d = deque([home])
#
#     if bfs():
#         print("happy")
#     else:
#         print("sad")


# DFS로 풀면 조건이 더 필요함!
from collections import deque
import sys

input = sys.stdin.readline

def dfs():
    while q:
        x, y = q.popleft()
        if abs(x-festival[0]) + abs(y-festival[1]) <= 1000:
            print("happy")
            return True
        for i in range(n):
            nx, ny = con[i]
            dis = abs(x-nx) + abs(y-ny)
            if dis <= 1000 and not visited[i]:
                visited[i] = 1
                q.append((nx, ny))
    print("sad")
    return False

for _ in range(int(input())):
    n = int(input())
    home = list(map(int, input().split()))
    con = [list(map(int, input().split())) for _ in range(n)]
    festival = list(map(int, input().split()))

    visited = [0]*n
    q = deque([home])
    dfs()