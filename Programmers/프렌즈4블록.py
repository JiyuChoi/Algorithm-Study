def check(board, i, j):
    cond = board[i][j]
    return (
            cond != "0"
            and board[i - 1][j] == cond
            and board[i][j - 1] == cond
            and board[i - 1][j - 1] == cond
    )


def solution(m, n, board):
    answer = 0
    board = [l[::-1] for l in list(map(list, zip(*board)))]
    dx, dy = [0, -1, 0, -1], [0, 0, -1, -1]

    while True:
        idx = set()
        for j in range(m - 1, 0, -1):
            for i in range(n - 1, 0, -1):
                if check(board, i, j):
                    for k in range(4):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        idx.add((nx, ny))
        if not idx:
            break
        idx_d = sorted(list(idx), reverse=True)
        for x, y in idx_d:
            del board[x][y]
            board[x].append("0")
            answer += 1

    return answer