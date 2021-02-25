from collections import deque
import copy
import sys
sys.setrecursionlimit(10000)

dx = [1,0,-1,0]
dy = [0,1,0,-1]
res = 0

def virus():
    global res
    v_lab = copy.deepcopy(lab)
    for i in range(n):
        for j in range(m):
            if v_lab[i][j] == 2:
                d.append((i,j))
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
    if cnt > res:
        res = cnt

def wall(s, l):
    if l == 3:
        virus()
        return
    else:
        for i in range(s, n*m):
            x = i // m
            y = i % m

            if lab[x][y] == 0:
                lab[x][y] = 1
                wall(i+1, l+1)
                lab[x][y] = 0


n, m = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
d = deque()

wall(0, 0)
print(res)