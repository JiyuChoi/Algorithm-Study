import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

stack = []
ch = [0]*(max(a)+1)
res = [-1]*n

# 데이터의 갑소가 동일한 인덱스의 데이터 1씩 증가
for i in a:
    try:
        ch[i] += 1
    except:
        ch[i] = 1

for i in range(n-1):
    stack.append(i)
    while stack and ch[a[stack[-1]]] < ch[a[i+1]]:
        res[stack.pop()] = a[i+1]

print(*res)