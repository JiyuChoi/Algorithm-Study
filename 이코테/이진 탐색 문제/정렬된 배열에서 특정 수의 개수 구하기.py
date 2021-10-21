# 이진탐색을 구현할 수 있는 라이브러리 O(logN)
from bisect import bisect_left, bisect_right

n, x = 8, 2
arr = [1,1,2,2,2,2,3,3]

res = bisect_right(arr, x)-bisect_left(arr, x)
if res:
    print(res)
else:
    print(-1)