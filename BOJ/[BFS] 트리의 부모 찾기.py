import sys

def bfs(start, link, arr):
    stack = [start]
    while stack:
        parent = stack.pop()
        for node in link[parent]:
            stack.append(node)
            arr[node].append(parent)
            link[node].remove(parent)
    return arr


n = int(sys.stdin.readline())
link = [[] for _ in range(n+1)]
arr = [[] for _ in range(n+1)]
stack = []

for _ in range(n-1):
    x, y = map(int, input().split())
    link[x].append(y)
    link[y].append(x)


for i in bfs(1, link, arr)[2:]:
    print(i[0])

