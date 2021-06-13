for t in range(int(input())):
    n = int(input())
    print(f'#{t+1}')
    print(1)
    res = [[1]]
    for i in range(1, n):
        arr = [1]
        for j in range(i-1):
            arr.append(res[i-1][j]+res[i-1][j+1])
        arr.append(1)
        res.append(arr)
        print(*arr)