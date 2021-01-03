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