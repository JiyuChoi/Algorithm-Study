n = int(input())
dy = [0,0,1,1]

for i in range(4, n+1):
    dy.append(dy[i-1] + 1)
    if i % 2 == 0:
        dy[i] = min(dy[i], dy[i//2]+1)
    if i % 3 == 0: #elif가 아닌 if로 가야함 6의 경우 3으로 나눈 값이 더 작음
        dy[i] = min(dy[i], dy[i//3]+1)

print(dy[n])