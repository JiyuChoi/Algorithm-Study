n = int(input())
bridge = [list(map(int, input().split())) for _ in range(n)]

dy = [[0]*n for _ in range(n)]
dy[0][0] = bridge[0][0]

# 가장자리(row, col = 0) 계산 입력
for i in range(1, n):
    dy[i][0] = dy[i-1][0] + bridge[i][0]
    dy[0][i] = dy[0][i-1] + bridge[0][i]

# 위, 왼쪽 중 최솟값을 찾아 dy에 더하기
for i in range(1, n):
    for j in range(1, n):
        dy[i][j] = min(dy[i-1][j], dy[i][j-1]) + bridge[i][j]

# 에너지 최소량 출력
print(dy[n-1][n-1])