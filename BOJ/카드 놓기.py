def dfs(l):
    if l == k:
        answer = ''
        for x in res:
            answer += str(x)
        ans.add(answer)

    else:
        for i in range(n):
            if ch[i] == 0:
                ch[i] = 1
                res[l] = num[i]
                dfs(l+1)
                ch[i] = 0

n = int(input())
k = int(input())

num = [int(input()) for _ in range(n)]
res = [0]*k
ch = [0]*n
ans = set()

dfs(0)
print(len(ans))