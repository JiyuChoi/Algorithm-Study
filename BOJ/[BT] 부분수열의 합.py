def dfs(l, sum):
    global cnt
    if l == n:
        if sum == s:
            cnt += 1

    else:
        dfs(l+1, sum+arr[l])
        dfs(l+1, sum)

n, s = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
dfs(0, 0)

# s가 0인 경우 공집합을 제외해줘야함!
print(cnt if s else cnt-1)