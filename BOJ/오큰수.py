# 수열의 크기 입력
n = int(input())
# 수열의 원소 입력
a = list(map(int, input().split()))

stack = []
answer = [-1]*n

for i in range(n-1):
    # idx 값을 stack에 추가
    stack.append(i)
    # stack에 값이 있고 a[stack[-1]]의 값이 a[i+1]보다 큰 경우
    while stack and a[stack[-1]] < a[i+1]:
        # stack에서 pop하고 answer에 a[i+1]값 입력
        answer[stack.pop()] = a[i+1]

print(*answer)