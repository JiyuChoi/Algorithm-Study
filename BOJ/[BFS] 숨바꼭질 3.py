from collections import deque

n, k = map(int, input().split())

max_s = 100001
visited = [0] * max_s
dis = [-1] * max_s

q = deque()
q.append(n)
dis[n] = 0
visited[n] = 1

while q:
    x = q.popleft()

    if x == k:
        print(dis[k])
        break

    if x*2 < max_s and not visited[x*2]:
        q.appendleft(x*2)
        visited[x*2] = 1
        dis[x*2] = dis[x]

    for nx in (x+1, x-1):
        if 0 <= nx < max_s and not visited[nx]:
            q.append(nx)
            visited[nx] = 1
            dis[nx] = dis[x] + 1