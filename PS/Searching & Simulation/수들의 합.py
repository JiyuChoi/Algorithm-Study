n, m = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
tot = 0
i = j = 0

while True:
    if tot < m:
        # 끝점이 n보다 작아야 되는 조건 필요!
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

# 다른 풀이
e = 0
# 시작점을 순차적으로 증가
for s in range(n):
    # 끝점을 가능한만큼 이동시키
    while tot < m and e < n:
        tot += num[e]
        e += 1
    # 부분합이 m이면 카운트 증가
    if tot == m:
        cnt += 1
    tot -= num[s]

print(cnt)