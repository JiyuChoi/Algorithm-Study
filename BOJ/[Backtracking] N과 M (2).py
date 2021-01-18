def dfs(l, s):
    if l == m:
        for i in ch:
            print(i, end=" ")
        print()

    else:
        for i in range(s, n + 1):
            ch[l] = i
            dfs(l + 1, i + 1)


n, m = map(int, input().split())
ch = [0] * m
dfs(0, 1)