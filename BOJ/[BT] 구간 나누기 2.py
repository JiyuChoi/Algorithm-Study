import sys
input = sys.stdin.readline

def isValid(mid):
    min_v = max_v = arr[0]
    cnt = 1

    for x in arr:
        if x > max_v:
            max_v = x
        if x < min_v:
            min_v = x
        if max_v - min_v > mid: # mid가 가장 작은 최댓값이 돼야하므로
            cnt += 1
            max_v = x
            min_v = x

    return m >= cnt

n, m = map(int, input().split())
arr = list(map(int, input().split()))

s = 0
e = max(arr)

res = float("inf")
while s<=e:
    mid = (s+e)//2
    if isValid(mid):
        e = mid - 1
        res = min(res, mid)
    else:
        s = mid + 1

print(res)