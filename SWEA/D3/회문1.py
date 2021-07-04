for t in range(10):
    l = int(input())
    board = [list(input()) for _ in range(8)]

    cnt = 0
    for i in range(9-l):
        for j in range(8):
            row = []
            col = []
            for k in range(i, i+l):
                row.append(board[j][k])
                col.append(board[k][j])
            if row == row[::-1]:
                cnt += 1
            if col == col[::-1]:
                cnt += 1

    print(f'#{t+1} {cnt}')