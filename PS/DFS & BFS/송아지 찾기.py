from collections import deque
s, e = map(int, input().split())
dis = [0]*10001
ch = [0]*10001
d = deque([s])

while d:
    now = d.popleft()
    if now == e:
        print(dis[now])
        break
    for dx in (1, -1, 5):
        nx = now + dx
        if 0<=nx<=10000:
            if ch[nx] == 0:
                ch[nx] = 1
                d.append(nx)
                dis[nx] = dis[now] + 1

# 5/7 풀이
s, e = map(int, input().split())
dis = [0]*10001
d = deque()
d.append(s)
dis[s] = 1

while d:
    now = d.popleft()
    if now == e:
        print(dis[e]-1)
        break
    for i in now+1, now-1, now+5:
        if 0<=i<=10001:
            d.append(i)
            dis[i] = dis[now] + 1
