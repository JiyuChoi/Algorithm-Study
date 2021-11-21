from collections import deque

def bfs():
    while d:
        x, y = d.popleft()
        if abs(festa[0]-x) + abs(festa[1]-y) <= 1000:
            return True
        for i in range(n):
            nx, ny = con[i]
            if abs(nx-x) + abs(ny-y) <= 1000 and not visited[i]:
                visited[i] = 1
                d.append((nx, ny))
    return False

for _ in range(int(input())):
    n = int(input())
    home = list(map(int, input().split()))
    con = [list(map(int, input().split())) for _ in range(n)]
    festa = list(map(int, input().split()))

    visited = [0]*n
    d = deque([home])

    if bfs():
        print("happy")
    else:
        print("sad")

