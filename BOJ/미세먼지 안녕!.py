import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
a = [list(map(int, input().saplit())) for _ in range(r)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(r):
    if a[i][0] == -1 and a[i+1][0] == -1:
        ac = (i, i+1)
        break

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

def upperbound():
    temp = a[ac[0]][c-1]
    for i in range(c-2, 0, -1):
        a[ac[0]][i+1] = a[ac[0]][i]

    temp2 = a[0][c-1]
    for i in range(ac[0]-1):
        a[i][c-1] = a[i+1][c-1]
    a[ac[0]-1][c-1] = temp

    temp3 = a[0][0]
    for i in range(c-1):
        a[0][i] = a[0][i+1]
    a[0][c-2] = temp2

    for i in range(ac[0]-1, 1, -1):
        a[i][0] = a[i-1][0]
    a[ac[0]][1] = 0
    a[1][0] = temp3

def lowerbound():
    temp = a[ac[1]][c-1]
    for i in range(c-2, 0, -1):
        a[ac[1]][i+1] = a[ac[1]][i]

    temp2 = a[r-1][c-1]
    for i in range(r-1, ac[1], -1):
        a[i][c-1] = a[i-1][c-1]
    a[ac[1]+1][c-1] = temp

    temp3 = a[r-1][0]
    for i in range(c-2):
        a[r-1][i] = a[r-1][i+1]
    a[r-1][c-2] = temp2

    for i in range(ac[1]+1, r-1):
        a[i][0] = a[i+1][0]
    a[ac[1]][1] = 0
    a[r-2][0] = temp3


for _ in range(t):
    spread()
    upperbound()
    lowerbound()

res = 0
for row in a:
    res += sum(row)

print(res+2)