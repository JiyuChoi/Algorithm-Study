for t in range(10):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    # 대각선의 합
    tot3, tot4 = 0, 0
    res = 0
    for i in range(100):
        # 행, 열의 합
        tot1, tot2 = 0, 0
        tot3 += board[i][i]
        tot4 += board[i][-(i+1)]
        for j in range(100):
            tot1 += board[i][j]
            tot2 += board[j][i]
        # 최댓값
        res = max(res, tot1, tot2, tot3, tot4)

    print(f'#{n} {res}')