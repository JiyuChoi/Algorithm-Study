from collections import deque

# 오른쪽 확인
def check_right(s, nd):
    if s > 4 or t[s][-2] == t[s-1][2]:
        return
    check_right(s+1, -nd)
    t[s].rotate(nd)

    # for i in range(n, 4):
    #     if t[i][2] != t[i+1][-2]:
    #         rotate[i+1] = -rotate[i]
    #     else:
    #         break

# 왼쪽 확인
def check_left(s, nd):
    if s < 1 or t[s][2] == t[s+1][-2]:
        return
    check_left(s-1, -nd)
    t[s].rotate(nd)

    # for i in range(n, 1, -1):
    #     if t[i][-2] != t[i-1][2]:
    #         rotate[i-1] = -rotate[i]
    #     else:
    #         break

t = [[]]
for _ in range(4):
    t.append(deque(map(int, input())))

k = int(input())
for _ in range(k):
    n, d = map(int, input().split())

    check_right(n+1, -d)
    check_left(n-1, -d)
    t[n].rotate(d)

res = 0
for i in range(4):
    res += t[i+1][0]*(2**i)

print(res)