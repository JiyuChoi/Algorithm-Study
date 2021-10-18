import sys

n = int(sys.stdin.readline())
d = list(map(int, sys.stdin.readline().split()))
p = list(map(int, sys.stdin.readline().split()))

res = 0
cur = p[0]

for i in range(1, n):
    res += d[i-1] * cur

    if cur > p[i]:
        cur = p[i]

print(res)

# 10/18 코드 깔끔하게 쓰는 연습!
n = int(input())
dis = list(map(int, sys.stdin.readline().split()))
pay = list(map(int, sys.stdin.readline().split()))
prev = pay[0]
res = 0

for i in range(1, n):
    res += prev * dis[i-1]
    if prev > pay[i]:
        prev = pay[i]
print(res)
