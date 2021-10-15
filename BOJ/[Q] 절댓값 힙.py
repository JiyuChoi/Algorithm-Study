# import heapq as hq
# import sys
#
# n = int(sys.stdin.readline())
# h = []
#
# for _ in range(n):
#     k = int(sys.stdin.readline())
#     if k != 0:
#         hq.heappush(h, (abs(k), k))
#     else:
#         # 여기서 try, except 써도 됨!
#         if len(h) > 0:
#             print(hq.heappop(h)[1])
#         else:
#             print(0)

import heapq as hq
import sys

n = int(sys.stdin.readline())
h = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        print(hq.heappop(h)[1] if h else 0)
    else:
        hq.heappush(h, (abs(num), num))
        #Q에 push할 때, 첫번째 값 기준 정렬 -> 두번째 값 기준 정렬로 들어감