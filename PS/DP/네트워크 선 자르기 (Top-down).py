def dfs(x):
    # 한 번 입력된 경우 dy값 출력
    if dy[x] > 0:
        return dy[x]
    if x == 1 or x == 2:
        return x
    else:
        dy[x] = dfs(x-1) + dfs(x-2)
        return dy[x]

n = int(input())
dy = [0]*(n+1)
print(dfs(n))
