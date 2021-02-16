from collections import deque
import sys

def bfs(v, target):
    cnt = 0
    q = deque([[v, cnt]])
    while q:
        value = q.popleft()
        v = value[0]
        cnt = value[1]
        if v == target:
            return cnt

        if not visited[v]:
            cnt += 1
            visited[v] = 1
            for e in link[v]:
                if not visited[e]:
                    q.append([e, cnt])
    return -1


n = int(sys.stdin.readline())
p1, p2 = map(int, sys.stdin.readline().split())
T = int(sys.stdin.readline())
link = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for _ in range(T):
    x, y = map(int, input().split())
    link[x].append(y)
    link[y].append(x)

print(bfs(p1, p2))