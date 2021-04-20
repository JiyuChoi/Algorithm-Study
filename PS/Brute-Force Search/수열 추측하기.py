import sys

def dfs(l, sum):
    if l == n and sum == f:
        print(*p)
        sys.exit(0)
    else:
        for x in range(1, n+1):
            if ch[x] == 0:
                ch[x] = 1
                p[l] = x
                dfs(l+1, sum+x*d[l])
                ch[x] = 0



n, f = map(int, input().split())
p = [0]*n
d = [1]*n
ch = [0]*(n+1)

for i in range(1, n):
    d[i] = d[i-1]*(n-i)//i
dfs(0,0)