n, c = map(int, input().split())
home = sorted([int(input()) for _ in range(n)])
s, e = 1, home[-1] - home[0]
res = 0
while s <= e:
    des = home[0]
    cnt = 1
    mid = (s+e)//2
    for h in home[1:]:
        if h - des >= mid:
            des = h
            cnt += 1
    if cnt >= c:
        res = mid
        s = mid + 1
    else:
        e = mid - 1
print(res)