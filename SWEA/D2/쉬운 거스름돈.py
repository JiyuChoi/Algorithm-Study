# 처음에는 list에 각 개수를 입력했는데,
# list에 저장할 필요 없이 바로 출력하면 빠름

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())
for t in range(1, T+1):
    n = int(input())
    print(f'#{t}')
    for i in range(len(money)):
        print(n // money[i], end=" ")
        n %= money[i]
    print()