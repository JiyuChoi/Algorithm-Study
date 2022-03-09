from collections import deque

n, k = map(int, input().split())
max_v = 100001
check = [-1] * max_v

q = deque()
q.append(n)

cnt = 0
check[n] = 0

while q:
    x = q.popleft()
    if x == k:
        cnt += 1
    for nx in (x*2, x+1, x-1):
        if 0 <= nx < max_v:
            if check[nx] == -1 or check[nx] >= check[x] + 1:
                check[nx] = check[x] + 1
                q.append(nx)

print(check[k])
print(cnt)