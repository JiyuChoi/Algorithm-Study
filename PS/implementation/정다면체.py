N, M = map(int, input().split())
answer = [0]*41

for i in range(1, N+1):
    for j in range(1, M+1):
        # 두수의 합을 index로 설정!
        answer[i+j] += 1

max_v = max(answer)

for i in range(41):
    if answer[i] == max_v:
        print(i, end=" ")