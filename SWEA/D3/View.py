for t in range(10):
    n = int(input())
    height = list(map(int, input().split()))
    res = 0

    for i in range(2, n-2):
        max_value = 0
        for k in (-2, -1, 1, 2):
            max_value = max(max_value, height[i+k])
        cha = height[i]-max_value
        if cha < 0:
            continue
        else:
            res += cha

    print(f'#{t+1} {res}')