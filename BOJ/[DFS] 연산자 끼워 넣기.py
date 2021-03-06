import sys

# 숫자 개수
n = int(sys.stdin.readline())
# 연산할 숫자 입력
a = list(map(int, sys.stdin.readline().split()))
# 연산자별 개수 입력
cal = list(map(int, sys.stdin.readline().split()))
ch = [0] * (n-1)
tot = []

def dfs(l):
    res = a[0]
    if l == n-1:
        for i in range(n-1):
            if ch[i] == 0:
                res += a[i+1]
            elif ch[i] == 1:
                res -= a[i+1]
            elif ch[i] == 2:
                res *= a[i+1]
            else:
                if res < 0 and a[i+1] > 0:
                    res = -(-res//a[i+1])
                else:
                    res //= a[i+1]
        tot.append(res)

    else:
        for i in range(4):
            if cal[i] != 0:
                ch[l] = i
                cal[i] -= 1
                dfs(l+1)
                ch[l] = 0
                cal[i] += 1


dfs(0)

print(max(tot))
print(min(tot))