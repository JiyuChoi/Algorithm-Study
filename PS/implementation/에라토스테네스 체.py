n = int(input())
number = [0] * (n+1)
cnt = 0

# 소수인 수의 개수를 구할 때 유용!
for i in range(2, n+1):
    if number[i] == 0:
        cnt += 1
        for j in range(i, n+1, i):
            number[j] = 1

print(cnt)