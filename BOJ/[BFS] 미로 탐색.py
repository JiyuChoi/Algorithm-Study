# import sys
# from collections import deque
#
# # BFS 풀이 (1) (시간이 적게 걸림)
# miro = []
# d = deque()
#
# # 방향벡터 설정
# dx = [1, 0, -1, 0]
# dy = [0, -1, 0, 1]
#
# # n, m 값 입력받기
# n, m = map(int, sys.stdin.readline().split())
#
# # miro 값 입력받기
# for i in range(n):
#     miro.append(list(map(int,input())))
#
# d.append([0,0])
# miro[0][0] = 0
#
# # 이동한 칸 개수 입력
# res = [[0]*m for _ in range(n)]
#
# while d:
#     now = d.popleft()
#     for i in range(4):
#         x = now[0] + dx[i]
#         y = now[1] + dy[i]
#         if 0 <= x < n and 0 <= y < m and miro[x][y] == 1:
#             miro[x][y] = 0
#             res[x][y] = res[now[0]][now[1]] + 1
#             d.append([x, y])
#
# else:
#     print(res[n-1][m-1]+1)
#
#
#
# # BFS 풀이 (2) (135ms 시간이 조금 더 걸림)
# n, m = map(int, input().split())
# ground = [list(map(int,input())) for _ in range(n)]
# d = deque()
# cnt = 0
#
# # 방향벡터 설정
# dx = [1,0,-1,0]
# dy = [0,-1,0,1]
#
#
# def bfs(x, y):
#     d = deque()
#     d.append((x, y))
#     # 큐가 빌 때까지 반복
#     while d:
#         x, y = d.popleft()
#         # 출구에 도착할 경우 최단거리 반환
#         if x == n-1 and y == m-1:
#             print(ground[x][y])
#             break
#         # 현재 위치에서 4방향으로 위치 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 미로 공간 내부에 있고 해당 노드를 처음 방문하는 경우
#             if 0<=nx<n and 0<=ny<m and ground[nx][ny]:
#                 ground[nx][ny] = ground[x][y] + 1
#                 d.append((nx, ny))
#
# bfs(0,0)

from collections import deque
n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

q = deque()
q.append((0, 0))

while q:
    x, y = q.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1
            q.append((nx, ny))

print(graph[n-1][m-1])
