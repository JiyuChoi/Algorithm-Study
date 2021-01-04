from collections import Counter
import sys

n = int(sys.stdin.readline())
num_n = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
num_m = list(map(int, sys.stdin.readline().split()))

cnt = Counter(num_n)

for i in num_m:
    print(cnt[i], end=" ")