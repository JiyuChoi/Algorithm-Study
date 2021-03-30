n, m = map(int, input().split())
song = list(map(int, input().split()))
s = 1
e = sum(song)
res = float("inf")

while s <= e:
    cnt = 1
    tot = 0
    mid = (s + e) // 2
    for x in song:
        tot += x
        if tot > mid:
            tot = x
            cnt += 1

    # 용량의 크기가 가장 크기가 큰곡 보다 작으면 안됨
    # 2장의 dvd에 들어가는 것은 3장에도 들어간다!
    if cnt <= m and mid >= max(song):
        res = mid
        e = mid - 1
    else:
        s = mid + 1

print(res)