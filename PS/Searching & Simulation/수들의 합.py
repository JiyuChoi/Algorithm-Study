n, m = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
tot = 0
i = j = 0

while True:
    if tot < m:
        if j < n:
            tot += num[j]
            j += 1
        else:
            break
    elif tot > m:
        tot -= num[i]
        i += 1
    else:
        cnt += 1
        tot -= num[i]
        i += 1

print(cnt)