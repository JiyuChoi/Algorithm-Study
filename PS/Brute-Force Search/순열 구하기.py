def dfs(l):
    global cnt
    if l == m:
        for x in res:
            print(x, end=" ")
        print()
        cnt += 1
    else:
        for i in range(1, n+1):
            if ch[i] == 0:
                ch[i] = 1
                res[l] = i
                dfs(l+1)
                ch[i] = 0


n, m = map(int, input().split())
ch = [0]*(n+1)
res = [0]*m
cnt = 0
dfs(0)
print(cnt)