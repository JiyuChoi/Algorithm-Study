from collections import deque

n, k = map(int, input().split())
d = deque([i+1 for i in range(n)])
res = []
cnt = 1

while d:
    p = d.popleft()
    if cnt == k:
        res.append(str(p))
        cnt = 1
    else:
        cnt += 1
        d.append(p)

print("<", ", ".join(res), ">", sep="")