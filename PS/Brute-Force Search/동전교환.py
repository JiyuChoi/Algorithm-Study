# cut-edge가 포인트! 안하면 시간초과
def dfs(sum, cnt):
    global min_value
    if cnt > min_value:
        return
    if sum > m:
        return
    if sum == m:
        if cnt < min_value:
            min_value = cnt
    else:
        for x in coin:
            dfs(sum+x, cnt+1)

n = int(input())
coin = list(map(int, input().split()))
m = int(input())
min_value = float("inf")
dfs(0, 0)
print(min_value)

