def dfs(l):
    global tot
    if l == k:
        return
    else:
        tot *= num
        dfs(l+1)

for _ in range(10):
    n = int(input())
    num, k = map(int, input().split())
    tot = 1
    dfs(0)
    print(f'#{n} {tot}')