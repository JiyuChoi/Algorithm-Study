def dfs(x, y):
    # 값이 입력된 경우 바로 리턴
    if dy[x][y] > 0:
        return dy[x][y]
    # (0,0)인 경우 값 입력
    if x == 0 and y == 0:
        return bridge[0][0]
    else:
        if x == 0:
            dy[x][y] = bridge[x][y] + dfs(x, y-1)
        elif y == 0:
            dy[x][y] = bridge[x][y] + dfs(x-1, y)
        else:
            dy[x][y] = min(dfs(x-1, y), dfs(x, y-1)) + bridge[x][y]
        return dy[x][y]


n = int(input())
bridge = [list(map(int, input().split())) for _ in range(n)]

dy = [[0]*n for _ in range(n)]

print(dfs(n-1, n-1))