# from collections import deque
# import copy
# import sys
# sys.setrecursionlimit(10000)
#
# dx = [1,0,-1,0]
# dy = [0,1,0,-1]
# res = 0
#
# def virus():
#     global res
#     v_lab = copy.deepcopy(lab)
#     for i in range(n):
#         for j in range(m):
#             if v_lab[i][j] == 2:
#                 d.append((i,j))
#     while d:
#         x, y = d.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<n and 0<=ny<m and not v_lab[nx][ny]:
#                 v_lab[nx][ny] = 2
#                 d.append((nx, ny))
#     cnt = 0
#     for l in v_lab:
#         cnt += l.count(0)
#     if cnt > res:
#         res = cnt
#
# def wall(s, l):
#     if l == 3:
#         virus()
#         return
#
#     else:
#         for i in range(s, n*m):
#             x = i // m
#             y = i % m
#
#             if lab[x][y] == 0:
#                 lab[x][y] = 1
#                 wall(i + 1, l + 1)
#                 lab[x][y] = 0
#
#
# n, m = map(int, sys.stdin.readline().split())
# lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# temp = [[0]*m for _ in range(n)]
# d = deque()
#
# wall(0, 0)
# print(res)
#
#
#
# # 밑의 방식을 이용하면 답은 나오지만 시간 초과
# def virus(i,j):
#     d.append((i,j))
#     while d:
#         x, y = d.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0<=nx<n and 0<=ny<m and not temp[nx][ny]:
#                 temp[nx][ny] = 2
#                 d.append((nx, ny))
#
# def get_score():
#     score = 0
#     for x in temp:
#         score += x.count(0)
#     return score
#
# def dfs(cnt):
#     global res
#     if cnt == 3:
#         for i in range(n):
#             for j in range(m):
#                 temp[i][j] = lab[i][j]
#
#         for i in range(n):
#             for j in range(m):
#                 if temp[i][j] == 2:
#                     virus(i,j)
#
#         res = max(get_score(), res)
#         return
#
#     else:
#         for i in range(n):
#             for j in range(m):
#                 if not lab[i][j]:
#                     lab[i][j] = 1
#                     cnt += 1
#                     dfs(cnt)
#                     lab[i][j] = 0
#                     cnt -= 1
#
# dfs(0)
# print(res)

import sys
from itertools import permutations
from collections import deque
import copy
input = sys.stdin.readline

def spread():
    global cnt
    while v:
        x, y = v.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not lab[nx][ny]:
                v.append((nx, ny))
                lab[nx][ny] = 2
    cnt = sum(l.count(0) for l in lab)
    return cnt

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
blank = []
virus = deque([])

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
answer = 0

for i in range(n):
    for j in range(m):
        if not graph[i][j]:
            blank.append((i, j))
        if graph[i][j] == 2:
            virus.append((i, j))

for p in permutations(blank, 3):
    lab = copy.deepcopy(graph)
    v = copy.deepcopy(virus)
    cnt = 0

    for x, y in p:
        lab[x][y] = 1

    cnt = spread()
    answer = max(cnt, answer)

print(answer)