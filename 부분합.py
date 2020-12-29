N, S = map(int, input().split())
num = list(map(int, input().split()))
lt = 0; rt = 1
tot = num[lt]
res = float('inf')
flag = False

while True:
    if tot >= S:
        res = min((rt - lt), res)
        tot -= num[lt]
        lt += 1
        flag = True

    else:
        if rt < N:
            tot += num[rt]
            rt += 1
        else:
            break

if flag:
    print(res)
else:
    print(0)