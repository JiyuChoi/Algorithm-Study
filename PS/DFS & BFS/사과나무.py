from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
apple = [list(map(int, input().split())) for _ in range(n)]

d = deque()
d.append((n//2, n//2))
tot = apple[n//2][n//2]
apple[n//2][n//2] = 0
L = 0

while d:
    if L == n//2:
        break
    size = len(d)
    for _ in range(size):
        x, y = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if apple[nx][ny] > 0:
                tot += apple[nx][ny]
                d.append((nx, ny))
                apple[nx][ny] = 0
    L += 1

print(tot)