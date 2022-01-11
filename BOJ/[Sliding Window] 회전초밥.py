from collections import defaultdict
import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr += arr[:k-1]

left = 0
cnt = 0
eat = defaultdict(int)
eat[c] = 1

for right in range(len(arr)):
    eat[arr[right]] += 1

    if right >= k-1:
        cnt = max(cnt, len(eat))
        eat[arr[left]] -= 1
        if eat[arr[left]] == 0:
            del eat[arr[left]]
        left += 1

print(cnt)
