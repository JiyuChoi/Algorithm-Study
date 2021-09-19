def dfs(s, l):
    if l == 6:
        for x in res:
            print(x, end=" ")
        print()
        return
    else:
        for i in range(s, n):
            res[l] = arr[i]
            s = i+1
            dfs(s, l+1)

while True:
    # n, *arr로 입력 받으면 정수, 리스트 받기 가능
    n, *arr = map(int, input().split())
    if n == 0:
        break
    res = [0]*6
    dfs(0, 0)
    print()