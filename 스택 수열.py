import sys

# n 입력 받기
n = int(sys.stdin.readline())
stack = []
ans = []
cnt = 1
tmp = 0

for _ in range(n):
    # 빼낼 수 입력
    num = int(sys.stdin.readline())

    # cnt가 빼낼 수보다 작거나 같다면 스택에 push
    while cnt <= num:
        stack.append(cnt)
        ans.append('+')
        cnt += 1

    # stack의 마지막 수가 빼낼 수가 아니라면 NO 출력
    if stack.pop() != num:
        tmp = 1

    # stack의 마지막 수 == 빼낼 수
    else:
        ans.append('-')

if tmp == 1:
    print("NO")
else:
    print("\n".join(ans))
