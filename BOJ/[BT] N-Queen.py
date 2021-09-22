# pypy로만 통과

def check(l):
    for x in range(l):
        if ch[x] == ch[l] or abs(ch[l]-ch[x]) == l-x:
            return False
    return True

def dfs(l):
    global cnt
    if l == n:
        cnt += 1
        return

    else:
        for i in range(n):
            if visited[i] == 0:
                ch[l] = i
                visited[i] = 1
                if check(l):
                    dfs(l+1)
                visited[i] = 0

n = int(input())
visited = [0]*n
ch = [0]*n
cnt = 0
dfs(0)
print(cnt)