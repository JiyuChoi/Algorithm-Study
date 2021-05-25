# 겹치는 숫자가 있는지 확인하는 함수
def check_num(board):
    for i in range(9):
        row_ch = [0]*10
        col_ch = [0]*10
        for j in range(9):
            # row, col별로 숫자 확인
            row_ch[board[i][j]] = 1
            col_ch[board[j][i]] = 1
        # 겹치는 숫자가 있다면 합이 9가 아니므로 0 리턴
        if sum(row_ch) != 9 or sum(col_ch) != 9:
            return 0

    for i in range(3):
        for j in range(3):
            box_ch = [0]*10
            for n in range(3*i, 3*(i+1)):
                for m in range(3*j, 3*(j+1)):
                    # 3*3 박스별로 숫자 확인
                    box_ch[board[n][m]] = 1
            # 겹치는 숫자가 있다면 합이 9가 아니므로 0 리턴
            if sum(box_ch) != 9:
                return 0
    # 모두 다른 숫자라면 1리턴
    return 1

# 테스트 케이스 입력
T = int(input())
for t in range(1, T+1):
    # 스도쿠 입력
    board = [list(map(int, input().split())) for _ in range(9)]
    print(f'#{t} {check_num(board)}')