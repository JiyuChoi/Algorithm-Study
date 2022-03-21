# n = int(input())
# dy = [0, 1, 3]
# for i in range(3, n + 1):
#     dy.append((dy[i-1] + 2*dy[i-2])%10007)
# print(dy[n])

n = int(input())
dy = [0]*1001
dy[1] = 1
dy[2] = 3

for i in range(3, n+1):
    dy[i] = dy[i-1] + dy[i-2]*2

print(dy[n]%10007)