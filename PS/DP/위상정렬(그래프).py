from collections import deque

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
d = deque()

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        d.append(i)

while d:
    now = d.popleft()
    print(now, end=" ")
    for j in graph[now]:
        if indegree[j] == 0:
            indegree[j] -= 1
            d.append(j)