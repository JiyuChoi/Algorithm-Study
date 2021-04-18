def dfs(l):
    if l == n:
        for i in range(n):
            if ch[i] == 1:
                print(i+1, end=" ")
        print()
    else:
        ch[l] = 1
        dfs(l+1)
        ch[l] = 0
        dfs(l+1)

n = int(input())
ch = [0]*n
dfs(0)
