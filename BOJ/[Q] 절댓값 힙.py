import heapq as hq
import sys

n = int(sys.stdin.readline())
h = []

for _ in range(n):
    k = int(sys.stdin.readline())
    if k != 0:
        hq.heappush(h, (abs(k), k))
    else:
        if len(h) > 0:
            print(hq.heappop(h)[1])
        else:
            print(0)