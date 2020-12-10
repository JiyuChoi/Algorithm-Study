N = int(input())
number = list(map(int, str(N)))
cnt = [0]*10

for i in number:
    if i in [6, 9]:
        cnt[6] += 1
    else:
        cnt[i] += 1

if cnt[6] % 2:
    cnt[6] = cnt[6]//2 + 1
else:
    cnt[6] = cnt[6]//2

print(max(cnt))