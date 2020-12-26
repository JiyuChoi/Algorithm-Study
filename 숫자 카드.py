import sys
n = int(sys.stdin.readline())
num_n = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
num_m = list(map(int, sys.stdin.readline().split()))

def binary_search(num_n, target, s, e):
    while s <= e:
        mid = (e + s) // 2
        if num_n[mid] > target:
            e = mid - 1
        elif num_n[mid] < target:
            s = mid + 1
        else:
            return 1
    else:
        return 0

for i in num_m:
    print(binary_search(num_n, i, 0, n-1), end=" ")