# import sys
# k, n = map(int, sys.stdin.readline().split())
# line = [int(sys.stdin.readline()) for _ in range(k)]
# s, e = 1, max(line) #s이 0이면 ZeroDivisionError 발생
# res = 0
#
# while s <= e:
#     mid = (s+e)//2
#     cnt = 0
#     for l in line:
#         cnt += l//mid
#     if cnt < n:
#         e = mid - 1
#     else:
#         s = mid + 1
#         res = mid
# print(res)

import sys
k, n = map(int, sys.stdin.readline().split())
line = [int(sys.stdin.readline()) for _ in range(k)]
s, e = 1, max(line)
res = 0

while s<=e:
    mid = (s+e)//2
    tot = sum(l//mid for l in line)
    if tot < n:
        e = mid - 1
    else:
        s = mid + 1
        res = mid
print(res)