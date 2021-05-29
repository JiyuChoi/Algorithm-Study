for t in range(1, int(input())+1):
    n = int(input())
    x = 0
    check = [0]*10
    while True:
        x += 1
        num = n*x
        for i in str(num):
            check[int(i)] = 1
        if sum(check) == 10:
            print(f'#{t} {num}')
            break