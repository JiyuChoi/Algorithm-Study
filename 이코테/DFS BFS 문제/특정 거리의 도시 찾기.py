from collections import deque

n, m, k, x = map(int, input().split())
visited = [0]*(n+1)
route = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    route[a].append(b)

d = deque([x])
while d:
    now = d.popleft()
    for next in route[now]:
        if visited[next] == 0:
            visited[next] = visited[now] + 1
            d.append(next)

flag = 0
for i in range(1, n+1):
    if visited[i] == k:
        print(i)
        flag = 1

if not flag:
    print(-1)