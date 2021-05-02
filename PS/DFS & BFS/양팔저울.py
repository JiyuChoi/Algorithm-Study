def dfs(l, tot):
    if l == n:
        if 0 < tot <= sum(weight):
            res.add(tot)
    else:
        dfs(l+1, tot - weight[l])
        dfs(l+1, tot + weight[l])
        dfs(l+1, tot)

n = int(input())
weight = list(map(int, input().split()))

res = set()
dfs(0,0)

print(sum(weight)-len(res))