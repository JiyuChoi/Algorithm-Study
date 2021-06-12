from collections import deque
for _ in range(10):
    n = int(input())
    d = deque(list(map(int, input().split())))
    print(f'#{n}', end=" ")

    i = 1
    while True:
        if i == 6:
            i = 1
        num = d.popleft()-i
        if num <= 0:
            d.append(0)
            break
        d.append(num)
        i += 1

    print(*d)