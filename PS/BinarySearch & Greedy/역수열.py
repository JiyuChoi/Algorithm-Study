n = int(input())
re_arr = list(map(int, input().split()))
arr = [0]*n

for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[j] == 0:
            if cnt == re_arr[i]:
                arr[j] = i+1
                break
            cnt += 1

print(*arr)
