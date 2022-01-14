# from collections import deque
# import sys
#
# # T값 입력 받기
# T = int(sys.stdin.readline())
#
# # 나이트 이동방향 설정
# dx = [2,2,1,1,-2,-2,-1,-1]
# dy = [1,-1,2,-2,1,-1,2,-2]
#
# for _ in range(T):
#     # 체스판의 길이 입력
#     l = int(sys.stdin.readline())
#     # 나이트의 현재 위치
#     night = tuple(map(int, sys.stdin.readline().split()))
#     # 나이트 목표 지점
#     des = tuple(map(int, sys.stdin.readline().split()))
#     # 이동횟수 기록
#     dis = [[0]*l for _ in range(l)]
#     d = deque()
#     d.append(night)
#
#     while d:
#         now = d.popleft()
#         # 현재 나이트의 위치가 목표 위치와 같다면 중지
#         if now == des:
#             # 그때의 거리 값 출력
#             print(dis[now[0]][now[1]])
#             break
#
#         for i in range(8):
#             x = now[0] + dx[i]
#             y = now[1] + dy[i]
#             # 체스판 범위를 벗어나지 않고 처음 방문한 경우
#             if 0<=x<l and 0<=y<l and dis[x][y] == 0:
#                 d.append((x,y))
#                 dis[x][y] = dis[now[0]][now[1]] + 1

1/14

from collections import deque

for _ in range(int(input())):
    l = int(input())
    x, y = map(int, input().split())
    target_x, target_y = map(int, input().split())

    board = [[-1]*l for _ in range(l)]
    board[x][y] = 0
    q = deque([(x, y)])

    dx = [1,1,-1,-1,2,2,-2,-2]
    dy = [2,-2,2,-2,1,-1,1,-1]

    while q:
        x, y = q.popleft()
        if (x, y) == (target_x, target_y):
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<l and 0<=ny<l and board[nx][ny] == -1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))

    print(board[target_x][target_y])