n = int(input())
num = list(map(int, input().split()))
num_rev = num[::-1]

inc = [1] * n
dec = [1] * n

for i in range(1, n):
    for j in range(i):
        if num[i] > num[j]:
            inc[i] = max(inc[i], inc[j]+1)
        if num_rev[i] > num_rev[j]:
            dec[i] = max(dec[i], dec[j]+1)

answer = 2
# for x, y in zip(inc, dec[::-1]):
#     answer = max(x+y, answer)
for i in range(n):
    answer = max(inc[i] + dec[n-i-1] - 1, answer)

print(answer)