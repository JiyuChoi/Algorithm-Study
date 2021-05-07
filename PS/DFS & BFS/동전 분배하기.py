def dfs(l):
    if l == n:
        global answer
        cha = max(res) - min(res)
        if cha < answer:
            tmp = set()
            for x in res:
                tmp.add(x)
            if len(tmp) == 3:
                answer = cha

    else:
        for i in range(3):
            res[i] += coin[l]
            dfs(l+1)
            res[i] -= coin[l]

n = int(input())
coin = [int(input()) for _ in range(n)]
res = [0]*3
answer = float("inf")
dfs(0)
print(answer)