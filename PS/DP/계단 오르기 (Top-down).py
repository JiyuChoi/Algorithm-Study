def dfs(x):
    if dy[x] > 0:
        return dy[x]
    if x == 1 or x == 2:
        return x
    else:
        dy[x] = dfs(x-1) + dfs(x-2)
        return dy[x]

n = int(input())

dy = [0]*(n+1)
dy[1] = 1
dy[2] = 2

print(dfs(n))
