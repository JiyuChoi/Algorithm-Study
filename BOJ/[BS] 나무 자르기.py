# python3로 하면 시간초과 pypy3는 가능
import sys
n, m = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))

s = 0; e = max(h); res = 0
while s <= e:
    total = 0
    mid = (s + e) // 2
    for x in h:
        if x > mid:
            total += x - mid
    if total < m:
        e = mid - 1
    else:
        res = mid
        s = mid + 1

print(res)

# python3으로 가능 (total 구하는 법을 바꿈)
import sys
n, m = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))

s, e = 0, max(height)
res = 0
while s <= e:
    total = 0
    mid = (s+e)//2
    total = sum(h-mid if h > mid else 0 for h in height)
    if total < m:
        e = mid - 1
    else:
        s = mid + 1
        res = mid
print(res)