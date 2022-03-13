from collections import deque
import sys

sys.setrecursionlimit(1000000000)

n, k = map(int, input().split())
max_s = 100001
visited = [False]*max_s
dis = [0]*max_s
move = [0]*max_s
q = deque()

q.append(n)
visited[n] = True

while q:
    x = q.popleft()

    if x == k:
        print(dis[k])
        break

    for nx in (x-1, x+1, x*2):
        if 0 <= nx < max_s and not visited[nx]:
            q.append(nx)
            visited[nx] = True
            dis[nx] = dis[x] + 1
            move[nx] = x

def print_route(n, k):
    if n != k:
        print_route(n, move[k])
    print(k, end=" ")

print_route(n, k)