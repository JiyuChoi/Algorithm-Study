n = int(input())
dy = [0]*100
brick = sorted([list(map(int, input().split())) for _ in range(n)], reverse=True)

dy[0] = brick[0][1]

for i in range(1, n):
    max_value = 0
    for j in range(i-1, -1, -1):
        if brick[i][2] < brick[j][2] and dy[j] > max_value:
            max_value = dy[j]
    dy[i] = max_value + brick[i][1]

print(max(dy))