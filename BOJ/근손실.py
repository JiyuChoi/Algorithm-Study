from itertools import permutations

n, k = map(int, input().split())
kits = list(map(int, input().split()))

cnt = 0

for p in permutations(kits, n):
    w = 500
    for kitweight in p:
        w = w - k + kitweight
        if w < 500:
            break
    else:
        cnt += 1

print(cnt)