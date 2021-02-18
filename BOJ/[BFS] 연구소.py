from collections import deque
import copy

dx = [1,0,-1,0]
dy = [0,1,0,-1]
max_val = 0

def virus():
    global max_val
    v_lab = copy.deepcopy(lab)
    for i in range(n):
        for j in range(m):
            if v_lab[i][j] == 2:
                d.append([i,j])
    while d:
        x, y = d.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not v_lab[nx][ny]:
                v_lab[nx][ny] = 2
                d.append((nx, ny))
    cnt = 0
    for l in v_lab:
        cnt += l.count(0)
    if cnt > max_val:
        max_val = cnt

def wall(x):
    if x == 3:
        virus()
        return
    for i in range(n):
        for j in range(m):
            if not lab[i][j]:
                lab[i][j] = 1
                wall(x+1)
                lab[i][j] = 0

n, m = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(n)]
d = deque()

wall(0)
print(max_val)
