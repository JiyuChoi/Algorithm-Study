import sys
import heapq as hq

n = int(sys.stdin.readline())
h = []

for _ in range(n):
    number = int(sys.stdin.readline())

    if number == 0:
        if not h:
            print(0)
        else:
            print(-hq.heappop(h))

    elif str(number).isdigit():
        hq.heappush(h, -number)