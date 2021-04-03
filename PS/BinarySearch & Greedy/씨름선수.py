n = int(input())
people = sorted([list(map(int, input().split())) for _ in range(n)], key=lambda x: (-x[0], -x[1]))

# 첫번째 정렬된 선수는 키가 가장 크므로 cnt += 1
standard = people[0][1]
cnt = 1
for p in people[1:]:
    # 만약 몸무게가 기준보다 크다면 cnt += 1
    if p[1] > standard:
        cnt += 1
    standard = p[1]

print(cnt)