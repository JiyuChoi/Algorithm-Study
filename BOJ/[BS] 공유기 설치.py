n, c = map(int, input().split())
house = sorted([int(input()) for _ in range(n)])

s, e = 1, (house[-1]-house[0])
res = 0

while s <= e:
    mid = (s+e)//2
    des = house[0]
    cnt = 1
    for h in house[1:]:
        if h - des >= mid:
           cnt += 1
           des = h
    if cnt < c:
        e = mid - 1
    else:
        s = mid + 1
        res = mid

print(res)