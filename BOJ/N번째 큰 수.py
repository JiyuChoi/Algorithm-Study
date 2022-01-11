import heapq as hq
h = []
n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    if not h:
        for x in arr:
            hq.heappush(h, x)
    else:
        for x in arr:
            if h[0] < x:
                hq.heappush(h, x)
                hq.heappop(h)
print(h[0])