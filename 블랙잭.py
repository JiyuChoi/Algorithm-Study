N, M = map(int, input().split())
card = sorted(list(map(int, input().split())))
ans = 0

for i in range(0, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            total = card[i] + card[j] + card[k]
            if total > M:
                break
            ans = max(total, ans)

print(ans)