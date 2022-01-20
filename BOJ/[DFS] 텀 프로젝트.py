#[순열 사이클]과 유사

# import sys
# sys.setrecursionlimit(1000000)
#
# def dfs(x):
#     global res
#     visited[x] = 1
#     cycle.append(x)
#     number = ch[x] # 다음 방문할 정점
#
#     if visited[number]:
#         if number in cycle:
#             res += cycle[cycle.index(number):]
#         return
#     else:
#         dfs(number)
#
# for _ in range(int(sys.stdin.readline())):
#     n = int(sys.stdin.readline())
#     ch = [0] + list(map(int, sys.stdin.readline().split()))
#     visited = [1] + [0] * n
#     res = []
#
#     for i in range(1, n+1):
#         if not visited[i]:
#             cycle = []
#             dfs(i)
#
#     print(n-len(res))

def dfs(v):
    global res
    cycle.append(v)
    visited[v] = 1
    next = student[v]
    if next in cycle:
        res += cycle[cycle.index(next):] #여기가 핵심포인트!
    if not visited[next]:
        dfs(next)
    return res

for _ in range(int(input())):
    n = int(input())
    student = [0] + list(map(int, input().split()))
    visited = [1] + [0]*n
    res = []
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n-len(res))
