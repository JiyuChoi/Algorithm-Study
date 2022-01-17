# from collections import deque
#
# def bfs():
#     while q:
#         now = q.popleft()
#         if now == g:
#             return True
#         # for next in (now + u, now - d):
#         #     if 0 < next <= f and not dis[next]: // 이 방법도 가능!
#         up = now + u
#         down = now - d
#         if up <= f and not dis[up]:
#             dis[up] = dis[now] + 1
#             q.append(up)
#         if down >= 0 and not dis[down]:
#             dis[down] = dis[now] + 1
#             q.append(down)
#     return False
#
# f, s, g, u, d = list(map(int, input().split()))
#
# dis = [0]*(f+1)
# q = deque()
# q.append(s)
# dis[s] = 1
#
# if bfs():
#     print(dis[g]-1)
# else:
#     print("use the stairs")


# 위의 풀이보다 간결한 풀이
from collections import deque

f, s, g, u, d = map(int, input().split())
h = f + 1
dis = [0]*h
dis[s] = 1

q = deque([s])
while q:
    now = q.popleft()
    if now == g:
        print(dis[g]-1)
        break
    for next in (now+u, now-d):
        if 0 < next <= f and not dis[next]:
            q.append(next)
            dis[next] = dis[now] + 1

else:
    print('use the stairs');