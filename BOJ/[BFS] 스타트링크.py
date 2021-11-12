from collections import deque

def bfs():
    while q:
        now = q.popleft()
        if now == g:
            return True
        up = now + u
        down = now - d
        if up <= f and not dis[up]:
            dis[up] = dis[now] + 1
            q.append(up)
        if down > 0 and not dis[down]:
            dis[down] = dis[now] + 1
            q.append(down)
    return False

f, s, g, u, d = list(map(int, input().split()))

dis = [0]*(f+1)
q = deque()
q.append(s)
dis[s] = 1

if bfs():
    print(dis[g]-1)
else:
    print("use the stairs")