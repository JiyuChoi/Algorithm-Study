import sys
import heapq as hq

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
indegree = [0]*(n+1)
h = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, n+1):
    if indegree[i] == 0:
        hq.heappush(h, i)

while h:
    now = hq.heappop(h)
    print(now, end=" ")
    for j in graph[now]:
        indegree[j] -= 1
        if indegree[j] == 0:
            hq.heappush(h, j)