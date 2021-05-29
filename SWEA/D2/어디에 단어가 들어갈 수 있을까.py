for t in range(1, int(input())+1):
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    # 행 기준 탐색
    for i in range(n):
        tot = 0
        for j in range(n):
            if board[i][j] == 0:
                if tot == k:
                    cnt += 1
                tot = 0
            else:
                tot += 1
        if tot == k:
            cnt += 1
    # 열 기준 탐색
    for i in range(n):
        tot = 0
        for j in range(n):
            if board[j][i] == 0:
                if tot == k:
                    cnt += 1
                tot = 0
            else:
                tot += 1
        if tot == k:
            cnt += 1

    print('#{} {}'.format(t, cnt))
