import sys

n = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split()))
p = list(map(int, sys.stdin.readline().split()))

res = 0
cur = p[0]

for i in range(1, n):
    res += d[i-1] * cur

    if cur > p[i]:
        cur = p[i]

print(res)