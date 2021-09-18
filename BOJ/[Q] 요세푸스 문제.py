from collections import deque

n, k = map(int, input().split())
d = deque([i+1 for i in range(n)])
res = []
cnt = 1

# deque 이용 방법 (시간이 오래걸림)
while d:
    p = d.popleft()
    if cnt == k:
        res.append(str(p))
        cnt = 1
    else:
        cnt += 1
        d.append(p)

# 제거할 수의 인덱스를 이용한 방법
num = 0
for _ in range(n):
    num += k-1
    if num >= len(d):
        num %= len(d)%num
    res.append(str(d.pop(num)))

print("<", ", ".join(res), ">", sep="")