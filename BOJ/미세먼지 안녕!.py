r, c, t = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(r)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def spread():
    tmp = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if a[x][y] >= 5:
                mess = a[x][y] // 5
                cnt = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < r and 0 <= ny < c and a[nx][ny] != -1:
                        tmp[nx][ny] += mess
                        cnt += 1
                # 나눠준 것만큼 뺀다
                a[x][y] = a[x][y] - mess * cnt

    for i in range(r):
        for j in range(c):
            # 추후에 받은 양 더하기
            a[i][j] += tmp[i][j]

def cleaner():
    for i in range(r):
        if a[i][0] == -1 and a[i+1][0] == -1:
            aircleaner = (i, i+1)
            break


for _ in range(t):
    cleaner()
    spread()
    for x in a:
        print(x)

