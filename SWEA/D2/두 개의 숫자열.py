for t in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr_n = list(map(int, input().split()))
    arr_m = list(map(int, input().split()))
    max_value = 0

    if n > m:
        n, m = m, n
        arr_n, arr_m = arr_m, arr_n

    for i in range(m-n+1):
        tot = 0
        for j in range(n):
            tot += arr_n[j] * arr_m[i+j]
        max_value = max(tot, max_value)

    print(f'#{t} {max_value}')