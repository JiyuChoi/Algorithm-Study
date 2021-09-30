import sys
n = int(input())
cost = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n):
    cost[i][0] = min(cost[i-1][1], cost[i-1][2]) + cost[i][0]
    cost[i][1] = min(cost[i-1][0], cost[i-1][2]) + cost[i][1]
    cost[i][2] = min(cost[i-1][0], cost[i-1][1]) + cost[i][2]

print(min(cost[n-1]))

# 9/30
n = int(input())
cost = [list(map(int, input().split())) for _ in range(n)]
dy = [[0]*3 for _ in range(n)] #col 3까지 설정 안하면 틀림!
dy[0] = cost[0]

for i in range(1, n):
    dy[i][0] = min(dy[i-1][1], dy[i-1][2]) + cost[i][0]
    dy[i][1] = min(dy[i-1][0], dy[i-1][2]) + cost[i][1]
    dy[i][2] = min(dy[i-1][0], dy[i-1][1]) + cost[i][2]

print(min(dy[n-1]))