n = int(input())
arr = list(map(int, input().split()))
cnt = 0

for x in arr:
    if x == 1:
        continue
    # int(x**0.5)+1 하면 탐색 시간 단축!
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            break
    else:
        cnt += 1

print(cnt)