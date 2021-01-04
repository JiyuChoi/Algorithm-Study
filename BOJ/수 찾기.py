import sys
input = sys.stdin.readline

def binary_search(num_n, target, s, e):
    while s <= e:
        mid = (s+e)//2
        if target < num_n[mid]:
            e = mid - 1
        elif target > num_n[mid]:
            s = mid + 1
        else:
            return 1
    else:
        return 0

n = int(input())
num_n = sorted(list(map(int, input().split())))
m = int(input())
num_m = list(map(int, input().split()))

for i in range(m):
    print(binary_search(num_n, num_m[i], 0, n-1))