def dfs(l):
    global cnt
    if l == n:
        cnt += 1
        for x in res:
            print(x, end=" ")
        print()
    else:
        for i in range(1, n+1):
            if visited[i] == 0 and route[l][i]:
                visited[i] = 1
                res.append(i)
                dfs(i)
                visited[i] = 0
                res.pop()

n, m = map(int, input().split())
route = [[0]*(n+1) for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    route[x][y] = 1

# 경로 입력
res = [1]
# 방문처리
visited[1] = 1

cnt = 0
dfs(1)
print(cnt)