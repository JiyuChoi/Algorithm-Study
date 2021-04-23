n = int(input())
coin = list(map(int, input().split()))
k = int(input())
dy = [1000]*(k+1)
dy[0] = 0
for i in range(n):
    c = coin[i]
    for j in range(c, k+1):
        dy[j] = min(dy[j], dy[j-c]+1)
print(dy[k])