def dfs(l, s, sum):
    global cnt
    if l == k and sum % m == 0:
        cnt += 1
    else:
        for i in range(s, n):
            dfs(l+1, i+1, sum+num[i])


n, k = map(int, input().split())
num = list(map(int, input().split()))
m = int(input())
cnt = 0
dfs(0, 0, 0)
print(cnt)
