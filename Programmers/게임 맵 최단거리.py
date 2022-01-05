from collections import deque


def solution(maps):
    answer = 0
    r = len(maps)
    c = len(maps[0])
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    dis = [[-1] * c for _ in range(r)]
    q = deque([(0, 0)])
    dis[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and maps[nx][ny] == 1:
                if dis[nx][ny] == -1:
                    dis[nx][ny] = dis[x][y] + 1
                    q.append((nx, ny))

    answer = dis[-1][-1]
    return answer