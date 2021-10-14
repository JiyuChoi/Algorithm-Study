import sys

n = int(sys.stdin.readline())
money = list(map(int, sys.stdin.readline().split()))
tot_money = int(sys.stdin.readline())

s, e = 1, max(money)
res = 0
while s <= e:
    mid = (s+e)//2
    total = sum(m if m < mid else mid for m in money)
    if total > tot_money:
        e = mid -1
    else:
        s = mid + 1
        res = mid
print(res)