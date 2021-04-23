n = int(input())
num = list(map(int, input().split()))
dy = [0]*n
dy[0] = 1
res = 0

for i in range(n):
    max_value = 0
    for j in range(i-1, 0, -1):
        if num[i] > num[j] and dy[j] > max_value:
            max_value = dy[j]
    dy[i] = max_value + 1
    res = max(res, dy[i])
print(res)