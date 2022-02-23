from collections import deque

n = int(input())
arr = list(map(int, input().split()))

res = [0]*n
q = deque()

for idx, v in enumerate(arr):
    q.append([idx, v])

cnt = 1
while q:
    q[0][1] -= 1
    if q[0][1] == 0:
        idx, v = q.popleft()
        res[idx] = cnt
    else:
        q.rotate(-1)
    cnt += 1

print(*res)