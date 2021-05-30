for t in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    board1 = [list(map(int, input().split())) for _ in range(n)]
    board2 = list(map(list, zip(*board1)))  # 배열 행과 열 전환
    cnt = 0

    for b in [board1, board2]:
        for x in b:
            str_list = ''.join(map(str, x)).split('0')
            for char in str_list:
                if char == '1'*k:
                    cnt += 1

    print('#{} {}'.format(t, cnt))