def move(cnt, dx, dy, direction):
    for _ in range(cnt+1):
        sx, sy = init['sx']+dx, init['sy']+dy
        init['sx'], init['sy'] = sx, sy
        if sx < 0 or sy < 0:
            break
        spreads = 0
        for dx, dy, r in rate[direction]:
            nx = sx + dx
            ny = sy + dy
            if r == 0:
                sand = graph[sx][sy] - spreads
            else:
                sand = int(graph[sx][sy]*r)
                spreads += sand
            if 0 <= nx < n and 0 <= ny < n:
                graph[nx][ny] += sand
            else:
                init['res'] += sand



n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

init = {'sx': n//2, 'sy': n//2, 'res': 0}

left = [(-2, 0, 0.02), (2, 0, 0.02), (-1, -1, 0.1), (-1, 0, 0.07), (-1, 1, 0.01), (1, -1, 0.1), (1, 0, 0.07), (1, 1, 0.01), (0, -2, 0.05), (0, -1, 0)]
right = [(x, -y, z) for x, y, z in left]
down = [(-y, x, z) for x, y, z in left]
up = [(-x, y, z) for x, y, z in down]

rate = {'left': left, 'right': right, 'down': down, 'up': up}

for i in range(n):
    if i % 2 == 0:
        move(i, 0, -1, 'left')
        move(i, 1, 0, 'down')
    else:
        move(i, 0, 1, 'right')
        move(i, -1, 0, 'up')
print(init['res'])

