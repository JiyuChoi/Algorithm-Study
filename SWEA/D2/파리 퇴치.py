T = int(input())
for k in range(1, T+1):
    n, m = map(int, input().split())
    # 배열 입력 받기
    board = [list(map(int, input().split())) for _ in range(n)]

    max_value = 0
    # 0부터 n-m까지 이동
    for i in range(n-m+1):
        for j in range(n-m+1):
            tot = 0
            # 파리채 m*m만큼 때림
            for x in range(i, i+m):
                for y in range(j, j+m):
                    tot += board[x][y]
            # 최대 파리 수이면 max_value로 설정
            if tot > max_value:
                max_value = tot

    print(f'#{k} {max_value}')