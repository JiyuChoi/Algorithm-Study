# def dfs(n):
#     global cnt
#     if n < a:
#         cnt = -1
#         return
#     elif n == a:
#         return
#     else:
#         if n % 10 == 1:
#             cnt += 1
#             dfs(n // 10)
#         else:
#             if n % 2 == 0:
#                 cnt += 1
#                 dfs(n // 2)
#             else:
#                 cnt = -1
#                 return

#dfs(n)

from collections import deque

a, b = map(int, input().split())

q = deque()
q.append((a, 1))

while q:
    x, cnt = q.popleft()
    if x == b:
        print(cnt)
        exit()

    if x*2 <= b:
        q.append((x*2, cnt + 1))
    x = int(str(x)+"1")
    if x <= b:
        q.append((x, cnt + 1))

print(-1)
