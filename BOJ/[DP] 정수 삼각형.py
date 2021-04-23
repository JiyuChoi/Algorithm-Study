n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]
dy[0][0] = tri[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dy[i][j] = dy[i-1][j] + tri[i][j]
        if j == i:
            dy[i][j] = dy[i-1][j-1] + tri[i][j]
        else:
            dy[i][j] = max(dy[i-1][j-1], dy[i-1][j]) + tri[i][j]

print(max(dy[n-1]))
