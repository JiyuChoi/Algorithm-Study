from collections import deque
n, c = map(int, input().split())
d = [i+1 for i in range(n)]
cnt = 0

while len(d) > 1:
    x = d.popleft() #d.pop(0)
    cnt += 1
    if cnt % c != 0:
        d.append(x)

print(d[0])


# 다른 풀이 deque 이용
d = deque(list(range(1, n+1)))
while d:
    for _ in range(c-1):
        x = d.popleft()
        d.append(x)
    d.popleft()
    if len(d) == 1:
        print(d[0])
        d.popleft()