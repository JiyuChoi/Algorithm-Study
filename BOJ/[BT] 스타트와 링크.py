# 처음 풀이 (9/21)
# ch2를 새로 만들고, for문을 여러번 돌려 깔끔하지 않은 것 같아 수정하려고 함
# 하지만 밑에 새로운 풀이가 시간이 더 오래걸림
def dfs(s, l):
    global res
    if l == n//2:
        ch2 = []
        start = link = 0
        for i in range(n):
            if i not in ch1:
                ch2.append(i)
        for x in ch1:
            for y in ch1:
                start += board[x][y]
        for x in ch2:
            for y in ch2:
                link += board[x][y]
        res = min(res, abs(start-link))
    else:
        for i in range(s, n):
            ch1[l] = i
            s = i+1
            dfs(s, l+1)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

ch1 = [0]*(n//2)
res = float("inf")
dfs(0, 0)
print(res)


# 이 방법이 메모리, 시간 더 오래걸림 (왜일까?)
def dfs(s, l):
    global res
    if l == n//2:
        start = link = 0
        for i in range(n):
            for j in range(n):
                if ch[i] and ch[j]:
                    start += board[i][j]
                elif not ch[i] and not ch[j]:
                    link += board[i][j]
        res = min(res, abs(start-link))
    else:
        for i in range(s, n):
            if ch[i] == 0:
                ch[i] = 1
                s = i+1
                dfs(s, l+1)
                ch[i] = 0