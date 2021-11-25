import copy

def watch(x, y, d, graph):
    for i in d:
        nx = x
        ny = y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] != 6:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = "#"
            else:
                break

def dfs(office, depth):
    global res
    if depth == len(cctv):
        cnt = 0
        for x in office:
            cnt += x.count(0)
        res = min(res, cnt)
        return
    x, y, dir = cctv[depth]
    tmp = copy.deepcopy(office)
    for d in direction[dir]:
        watch(x, y, d, tmp)
        dfs(tmp, depth+1)
        tmp = copy.deepcopy(office)



n, m = map(int, input().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction = [[],
             [[0], [1], [2], [3]],
             [[0, 2], [1, 3]],
             [[0, 1], [1, 2], [2, 3], [3, 0]],
             [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
             [[0, 1, 2, 3]]]

office = []
cctv = []
res = float("inf")
for i in range(n):
    arr = list(map(int, input().split()))
    office.append(arr)
    for j in range(m):
        if arr[j] != 0 and arr[j] != 6:
            cctv.append((i, j, arr[j]))

dfs(office, 0)
print(res)