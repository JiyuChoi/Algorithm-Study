n = int(input())
num = list(map(int, input().split()))

dy = [0]*n
dy[0] = 1
res = 0

for i in range(n):
    max_value = 0
    for j in range(i-1, 0, -1):
        # 앞에 수보다 크고 dy 값이 max_value 보다 큰 경우 (반복해서 max_value를 찾는 것)
        if num[i] > num[j] and dy[j] > max_value:
            max_value = dy[j]
    # 최대값에 하나 더하기
    dy[i] = max_value + 1
    res = max(res, dy[i])

print(res)