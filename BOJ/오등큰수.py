import sys
from collections import Counter

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

stack = []
res = [-1]*n

# 내장 클래스 Counter를 이용한 더 간결한 방식
count = Counter(a)
ch = [count[i] for i in a]


for i in range(n-1):
    stack.append(i)
    while stack and ch[a[stack[-1]]] < ch[a[i+1]]:
        res[stack.pop()] = a[i+1]

print(*res)



'''
# check 리스트 선언
ch = [0]*(max(a)+1)

# 데이터의 값과 동일한 인덱스의 데이터 1씩 증가
for i in a:
    try:
        ch[i] += 1
    except:
        ch[i] = 1
'''
