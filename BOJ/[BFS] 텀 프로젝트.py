import sys
sys.setrecursionlimit(1000000)

def dfs(x):
    global res
    visited[x] = 1
    cycle.append(x)
    number = ch[x] # 다음 방문할 정점

    if visited[number]:
        if number in cycle:
            res += cycle[cycle.index(number):]
        return
    else:
        dfs(number)

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    ch = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [1] + [0] * n
    res = []

    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)

    print(n-len(res))