def dfs(l, res, tot):
    global max_v
    if tot > m:
        return
    if l == n:
        if res > max_v:
            max_v = res
    else:
        dfs(l+1, res+score[l], tot+time[l])
        dfs(l+1, res, tot)

n, m = map(int, input().split())
score, time = [], []
for _ in range(n):
    s, t = map(int, input().split())
    score.append(s)
    time.append(t)
max_v = float("-inf")
dfs(0,0,0)
print(max_v)