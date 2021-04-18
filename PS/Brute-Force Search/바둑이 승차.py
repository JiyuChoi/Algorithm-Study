def dfs(l, sum):
    global max_value
    if sum > c:
        return
    if l == n:
        if sum > max_value:
            max_value = sum
    else:
        dfs(l+1, sum + w[l])
        dfs(l+1, sum)

c, n = map(int, input().split())
w = [int(input()) for _ in range(n)]
max_value = float("-inf")
dfs(0,0)
print(max_value)