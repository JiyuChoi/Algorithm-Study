# 1948
days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(1, int(input())+1):
    m1, d1, m2, d2 = map(int, input().split())
    if m1 == m2:
        res = d2-d1
    else:
        res = (days[m1]-d1)+d2
        for i in range(m1+1, m2):
            res += days[i]
    print(f'#{t} {res+1}')