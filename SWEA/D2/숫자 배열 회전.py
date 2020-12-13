for t in range(1, int(input())+1):
    n = int(input())
    number = [list(map(int, input().split())) for _ in range(n)]

    print(f'#{t}')
    for i in range(n):
        d90, d180, d270 = '', '', ''
        for j in range(n):
            # 90도 회전한 경우
            d90 += str(number[-(j+1)][i])
            # 180도 회전한 경우
            d180 += str(number[-(i+1)][-(j+1)])
            # 270도 회전한 경우
            d270 += str(number[j][-(i+1)])

        print(d90, d180, d270)