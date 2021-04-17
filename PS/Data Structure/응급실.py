from collections import deque
n, m = map(int, input().split())
d = [(idx, val) for idx, val in enumerate(list(map(int, input().split())))]
d = deque(d)
cnt = 0

while True:
    cur = d.popleft()
    if any(cur[1] < x[1] for x in d):
        d.append(cur)
    else:
        cnt += 1
        if cur[0] == m:
            print(cnt)
            break
