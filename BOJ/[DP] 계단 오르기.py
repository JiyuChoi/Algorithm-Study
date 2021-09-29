n = int(input())
score = [int(input()) for _ in range(n)]
dy = [0]*n

if n == 1:
    print(score[0])
else:
    dy[0] = score[0]
    dy[1] = score[0] + score[1]
    for i in range(2, n):
        dy[i] = max(dy[i-3]+score[i-1]+score[i], dy[i-2]+score[i])
    print(dy[-1])