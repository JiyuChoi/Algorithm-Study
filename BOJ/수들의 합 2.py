n, m = map(int, input().split())
arr = list(map(int, input().split()))

s, e = 0, 0
answer = 0

while s <= e and e <= n:
    tot = sum(arr[s:e])
    if tot > m:
        s += 1
    else:
        if tot == m:
            answer += 1
        e += 1
print(answer)