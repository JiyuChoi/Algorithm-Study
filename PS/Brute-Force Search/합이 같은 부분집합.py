import sys
def dfs(l, sum):
    if tot // 2 < sum:
        return
    if l == n:
        # tot가 홀수이면 yes인 경우 나올 수 없음 => tot//2 = sum이라 하면 안됨!
        if tot - sum == sum:
            print("YES")
            sys.exit(0)
    else:
        dfs(l+1, sum + num[l])
        dfs(l+1, sum)

n = int(input())
num = list(map(int, input().split()))
tot = sum(num)
dfs(0, 0)
print("NO")