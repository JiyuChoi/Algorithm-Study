from collections import deque
import sys
input = sys.stdin.readline

n, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr += arr[:k-1]
q = deque([])

answer = 0
start = 0
for end, val in enumerate(arr):
    q.append(val)
    if end - start + 1 == k:
        susi = set(list(q))
        susi.add(c)
        if len(susi) > answer:
            answer = len(susi)
        q.popleft()
        start += 1

print(answer)
