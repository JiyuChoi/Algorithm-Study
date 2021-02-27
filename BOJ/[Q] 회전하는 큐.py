# deque 이용 풀이
from collections import deque

n, m = map(int, input().split())
index = map(int, input().split())

num = [i+1 for i in range(n)]
d = deque(num)
cnt = 0

def left_pop():
    global cnt
    while True:
        now = d.popleft()
        if now == target:
            return
        else:
            d.append(now)
            cnt += 1

def right_pop():
    global cnt
    while True:
        now = d.pop()
        d.appendleft(now)
        cnt += 1
        if now == target:
            d.popleft()
            return

for idx in index:
    l = len(d) // 2
    target = num[idx-1]
    if d.index(target) <= l:
        left_pop()
    else:
        right_pop()

print(cnt)


### idx split를 이용한 풀이 (시간이 더 빠름)
for idx in index:
    numIdx = num.index(idx)
    if numIdx <= len(num)//2:
        cnt += len(num[:numIdx])
        num = num[numIdx+1:] + num[:numIdx]
    else:
        cnt += len(num[numIdx:])
        num = num[numIdx+1:] + num[:numIdx]

print(cnt)