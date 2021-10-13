import sys
n = int(input())
w = sorted([int(sys.stdin.readline()) for _ in range(n)], reverse=True)

res = 0
for i in range(len(w)):
    res = max(res, w[i]*(i+1))
print(res)