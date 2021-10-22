def binary_search(arr, s, e):
    if s > e:
        return None
    mid = (s+e)//2
    if arr[mid] == mid:
        return mid
    elif arr[mid] > mid:
        binary_search(arr, s, mid - 1)
    else:
        binary_search(arr, mid + 1, e)

n = int(input())
arr = list(map(int, input().split()))

idx = binary_search(arr, 0, n)

if idx == None:
    print(-1)
else:
    print(idx)