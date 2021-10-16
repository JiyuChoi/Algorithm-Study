import heapq as hq
import sys

n = int(input())
right, left = [], []
for _ in range(n):
    num = int(sys.stdin.readline())
    if len(right) == len(left):
        hq.heappush(left, (-num, num))
    else:
        hq.heappush(right, (num, num))

    if right and left[0][1] > right[0][1]:
        left_v = hq.heappop(left)[1]
        right_v = hq.heappop(right)[1]
        hq.heappush(right, (left_v, left_v))
        hq.heappush(left, (-right_v, right_v))

    print(left[0][1])