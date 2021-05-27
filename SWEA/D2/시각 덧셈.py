for t in range(1, int(input())+1):
    h1, m1, h2, m2 = map(int, input().split())
    # 시간, 분 더하기
    h = h1 + h2
    m = m1 + m2

    # 분이 60을 넘으면
    if m >= 60:
        h += m // 60
        m = m%60
    # 시간이 12를 넘으면
    if h > 12:
        h -= 12

    print(f'#{t} {h} {m}')