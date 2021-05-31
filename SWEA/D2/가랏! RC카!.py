for t in range(1, int(input())+1):
    n = int(input())
    s = 0
    v = 0
    for _ in range(n):
        command = list(map(int, input().split()))
        if command[0] == 1:
            v += command[1]
            s += v
        elif command[0] == 2:
            v -= command[1]
            if 0 >= v:
                v = 0
            s += v
        else:
            s += v

    print(f'#{t} {s}')