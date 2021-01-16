def dfs(l):
    if l == m:
        for i in res:
            print(i, end=" ")
        print()

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
dfs(0)