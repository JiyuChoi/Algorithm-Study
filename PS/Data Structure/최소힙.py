import heapq as hq

h = []

while True:
    n = int(input())
    if n == 0:
        if not h:
            print(-1)
        else:
            print(hq.heappop(h))
    elif n == -1:
        break
    else:
        hq.heappush(h, n)