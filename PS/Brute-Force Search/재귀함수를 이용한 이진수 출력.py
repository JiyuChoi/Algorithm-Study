def dfs(n):
    if n < 1:
        return
    else:
        dfs(n//2)
        print(n%2, end="")

dfs(11)