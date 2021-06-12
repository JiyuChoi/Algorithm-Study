from collections import deque
for _ in range(10):
    n = int(input())
    d = deque(list(map(int, input().split())))
    print(f'#{n}', end=" ")
    flag = False
    while 0 not in d:
        if flag:
            break
        for i in range(5):
            num = d.popleft()-(i+1)
            if num <= 0:
                flag = True
                d.append(0)
                break
            d.append(num)
    print(*d)