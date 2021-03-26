n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
m = int(input())

for i in range(m):
    r, d, cnt = map(int, input().split())
    if d:
        for _ in range(cnt):
            board[r-1].insert(0, board[r-1].pop())
    else:
        for _ in range(cnt):
            board[r-1].append(board[r-1].pop(0))

s = 0
e = n
res = 0
for i in range(n):
    res += sum(board[i][s:e])
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(res)