import sys
import heapq as hq

input = sys.stdin.readline

N, K = map(int, input().split())
jewel = []
bag = []
for _ in range(N):
    hq.heappush(jewel, list(map(int, input().split())))
for _ in range(K):
    bag.append(int(input()))

bag.sort()

res = 0
tmp = []
for b in bag:
    while jewel and b >= jewel[0][0]:
        hq.heappush(tmp, -hq.heappop(jewel)[1])

    if tmp:
        res -= hq.heappop(tmp)

print(res)