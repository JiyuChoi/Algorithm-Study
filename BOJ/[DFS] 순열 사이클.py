# [텀 프로젝트]와 유사
import sys
sys.setrecursionlimit(1000000)

def dfs(v):
    global cnt
    visited[v] = 1
    cycle.append(v)
    next = route[v]
    if visited[next]:
        if next in cycle:
            cnt += 1
    else:
        dfs(next)

for _ in range(int(input())):
    n = int(input())
    route = [0] + list(map(int, input().split()))
    visited = [1] + [0] * n
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:

            cycle = []
            dfs(i)

    print(cnt)