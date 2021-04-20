def dfs(l, s):
    global cnt
    if l == m:
        for x in ch:
            print(x, end=" ")
        print()
        cnt += 1
    else:
        for i in range(s, n+1):
            ch[l] = i
            dfs(l+1, i+1)


n, m = map(int, input().split())
ch = [0]*m
cnt = 0
dfs(0, 1)
print(cnt)
