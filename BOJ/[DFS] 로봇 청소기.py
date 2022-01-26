# def clean(x, y, d):
#     global cnt
#     for _ in range(4):
#         nd = (d + 3) % 4
#         nx = x + dx[nd]
#         ny = y + dy[nd]
#         if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0:
#             board[nx][ny] = 2
#             cnt += 1
#             clean(nx, ny, nd)
#             return
#         d = nd
#
#     nd = (d + 2) % 4
#     nx = x + dx[nd]
#     ny = y + dy[nd]
#     if board[nx][ny] == 1: # 뒤에 벽인 경우
#         return
#     clean(nx, ny, d) # 2번을 시행할 수 있는 경우
#
# n, m = map(int, input().split())
# r, c, d = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
#
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
#
# cnt = 1
# board[r][c] = 2
# clean(r, c, d)
#
# print(cnt)

def clean(x, y, d):
    global cnt
    for _ in range(4):
        nd = (d+3)%4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if 0<=nx<n and 0<=ny<m and board[nx][ny] == 0:
            board[nx][ny] = 2
            cnt += 1
            clean(nx, ny, nd)
            return
        d = nd

    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if board[nx][ny] == 1:
        return
    clean(nx, ny, d)


n, m = map(int, input().split())
r, c, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

cnt = 1
board[r][c] = 2
clean(r, c, d)

print(cnt)