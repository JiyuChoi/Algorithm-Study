from collections import deque

def route(x):
    arr = []
    for _ in range(dis[x] + 1):
        arr.append(x)
        x = move[x]
    print(*arr[::-1])

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
        route(x)
        break

    for nx in (x-1, x+1, x*2):
        if 0 <= nx < max_s and not visited[nx]:
            q.append(nx)
            visited[nx] = True
            dis[nx] = dis[x] + 1
            move[nx] = x

print(move)