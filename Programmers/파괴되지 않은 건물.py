def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    arr = [[0] * (m + 1) for i in range(n + 1)]

    for s in skill:
        tp, r1, c1, r2, c2, d = s
        if tp == 1:
            d = -d
        arr[r1][c1] += d
        arr[r1][c2 + 1] -= d
        arr[r2 + 1][c1] -= d
        arr[r2 + 1][c2 + 1] += d

    for i in range(n):
        for j in range(1, m):
            arr[i][j] += arr[i][j - 1]

    for i in range(1, n):
        for j in range(m):
            arr[i][j] += arr[i - 1][j]

    for i in range(n):
        for j in range(m):
            if arr[i][j] + board[i][j] > 0:
                answer += 1

    return answer