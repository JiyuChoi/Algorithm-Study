T = int(input())

for t in range(1, T+1):
    n = int(input())
    tot = 0
    for i in range(1, n+1):
        if i%2:
            tot += i
        else:
            tot -= i
    print(f'#{t} {tot}')