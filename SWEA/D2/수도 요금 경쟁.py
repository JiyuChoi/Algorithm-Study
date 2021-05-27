T = int(input())
for t in range(1, T+1):
    p, q, r, s, w = map(int, input().split())
    # a, b 수도 기본 요금
    a = w*p
    b = q
    # r리터 이상 사용시 추가 요금 계산
    if w > r:
        b += (w-r)*s

    # b력 요금이 더 적다면 b 출력
    if a > b:
        print(f'#{t} {b}')
    else:
        print(f'#{t} {a}')