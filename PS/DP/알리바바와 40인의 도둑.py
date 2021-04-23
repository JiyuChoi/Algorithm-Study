n = int(input())
bridge = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]*n for _ in range(n)]
dy[0][0] = bridge[0][0]

for i in range(1, n):
    dy[i][0] = bridge[i][0] + dy[i-1][0]
    dy[0][i] = bridge[0][i] + dy[0][i-1]

for i in range(1, n):
    for j in range(1, n):
        dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + bridge[i][j]

print(dy[n-1][n-1])