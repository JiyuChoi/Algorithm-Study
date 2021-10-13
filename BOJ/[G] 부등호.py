def check(n1, arr, n2):
    if arr == '>':
        return n1 > n2
    else:
        return n1 < n2

def dfs(l, s):
    global ans
    if l == n+1:
        ans.append(s)
        return
    for i in range(10):
        if ch[i] == 0:
            if l == 0 or check(int(s[-1]), arr[l-1], i):
                ch[i] = 1
                dfs(l+1, s+str(i))
                ch[i] = 0

n = int(input())
arr = input().split()
ch = [0]*10
ans = []
dfs(0, "")
print(ans[-1])
print(ans[0])