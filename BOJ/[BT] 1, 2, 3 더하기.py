def dfs(sum):
    global cnt
    if sum >= n:
        if sum == n:
            cnt += 1
        return
    else:
        for i in range(3):
            dfs(sum+(i+1))


t = int(input())
for _ in range(t):
    n = int(input())
    cnt = 0
    dfs(0)
    print(cnt)