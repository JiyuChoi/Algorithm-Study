for t in range(1, int(input())+1):
    n = int(input())
    print(f'#{t}', end=" ")
    for i in (2, 3, 5, 7, 11):
        k = 0
        while n%i == 0:
            n = n//i
            k += 1
        # 따로 저장할 필요없이 바로 출력!
        print(k, end=" ")
    print()