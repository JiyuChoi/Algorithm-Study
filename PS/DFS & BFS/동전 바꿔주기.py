def dfs(l, sum):
    global cnt
    if l == k:
        if sum == t:
            cnt += 1
    else:
        # l 이용해 index 대신 사용!
        for i in range(num[l]+1):
            dfs(l+1, sum + cost[l]*i)

t = int(input())
k = int(input())
cost, num = [], []
for _ in range(k):
    p, n = map(int, input().split())
    cost.append(p)
    num.append(n)

cnt = 0
dfs(0, 0)
print(cnt)