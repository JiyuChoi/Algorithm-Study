# from collections import deque
#
# n, k = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
# target_s, target_x, target_y = map(int, input().split())
# virus = []
#
# # 방향벡터 설정
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
#
# # virus 리스트에 바이러스 종류별 위치 저장
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] != 0:
#             virus.append((graph[i][j], 0, i, j))
#
# # 1부터 시작되게 정렬
# virus.sort()
# d = deque(virus)
#
#
# while d:
#     # 바이러스 종류, cnt, x좌표, y좌표 (따로 변수로 받아주는게 중요!)
#     v, s, x, y = d.popleft()
#     # s == cnt이면 정지
#     if s == target_s:
#         break
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0<=nx<n and 0<=ny<n and not graph[nx][ny]:
#             # v로 인해 전염
#             graph[nx][ny] = v
#             # d에 추가 (cnt + 1)
#             d.append((v, s+1, nx, ny))
#
#
# print(graph[target_x-1][target_y-1])



from collections import deque

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
s, x, y = map(int, input().split())

q = deque([])
for i in range(n):
    for j in range(n):
        if not board[i][j]:
            q.append((i, j. board[i][j]))









