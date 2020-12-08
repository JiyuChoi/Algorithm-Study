N = int(input())

if i < 100:
    cnt = i

else:
    cnt = 99
    for i in range(100, N+1):
        number = list(map(int, str(i)))
        if number[2] - number[1] == number[1] - number[0]:
            cnt += 1

print(cnt)