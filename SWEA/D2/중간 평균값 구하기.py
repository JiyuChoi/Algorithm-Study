T = int(input())

for i in range(1, T+1):
    number = sorted(list(map(int, input().rstrip().split())))
    number.pop() #O(1)
    number.pop(0) #O(n)
    # 반올림 round
    print(f'#{i} {round(sum(number)/8)}')