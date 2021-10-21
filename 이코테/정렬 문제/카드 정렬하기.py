import heapq as hq
import sys

n = int(sys.stdin.readline())
h = []
for _ in range(n):
    hq.heappush(h, int(sys.stdin.readline()))

res = 0
while len(h) != 1:
    first = hq.heappop(h)
    second = hq.heappop(h)
    tot = first + second
    hq.heappush(h, tot)
    res += tot

print(res)