## 간단한 풀이
import sys

# 숫자 개수
n = int(sys.stdin.readline())
# 연산할 숫자 입력
data = list(map(int, sys.stdin.readline().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1

# 메서드 호출
dfs(1, data[0])

# 최솟값, 최댓값 출력
print(max_value)
print(min_value)



## 처음 풀이
# 숫자 개수
n = int(sys.stdin.readline())
# 연산할 숫자 입력
data = list(map(int, sys.stdin.readline().split()))
# 연산자별 개수 입력
cal = list(map(int, sys.stdin.readline().split()))
ch = [0] * (n-1)
tot = []

def dfs(l):
    res = a[0]
    if l == n-1:
        for i in range(n-1):
            if ch[i] == 0:
                res += data[i+1]
            elif ch[i] == 1:
                res -= data[i+1]
            elif ch[i] == 2:
                res *= data[i+1]
            else:
                if res < 0 and data[i+1] > 0:
                    res = -(-res//data[i+1])
                else:
                    res //= data[i+1]
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
