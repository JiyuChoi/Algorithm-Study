n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
res = 0
for c in coins[::-1]:
    res += k//c
    k = k%c
print(res)