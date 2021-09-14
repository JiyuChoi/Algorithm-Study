# N = 10,000,000 / 메모리 8MB 인 경우
# 메모리 초과가 날 수도 있음. 이 경우 list로 값을 check!

import sys

n = int(sys.stdin.readline())
arr = [0]*10001
for _ in range(n):
    m = int(sys.stdin.readline())
    arr[m] += 1

for i in range(10001):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)
