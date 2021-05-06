import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
q = deque()
res = []

for _ in range(m):
    a, b = map(int, input().split())
    indegree[b] += 1
    graph[a].append(b)


for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)


while q:
    now = q.popleft()
    res.append(now)
    for j in graph[now]:
        indegree[j] -= 1
        if indegree[j] == 0:
            q.append(j)

print(*res)

