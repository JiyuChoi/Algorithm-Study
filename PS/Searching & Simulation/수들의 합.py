n, m = map(int, input().split())
num = list(map(int, input().split()))
s = e = 0
cnt = 0
tot = 0
while True:
    if tot < m:
        if e < n:
            tot += num[e]
            e += 1
        else:
            break
    elif tot > m:
        tot -= num[s]
        s += 1
    else:
        cnt += 1
        tot -= num[s]
        s += 1

print(cnt)