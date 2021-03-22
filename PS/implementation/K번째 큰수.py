n, k = map(int, input().split())
num = list(map(int, input().split()))
res = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            tot = num[i] + num[j] + num[m]
            # 중복제거를 위해 set에 추가
            res.add(tot)

print(sorted(list(res))[-k])
