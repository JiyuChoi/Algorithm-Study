T = int(input())
for t in range(1, T+1):
    n = int(input())
    strs = ''

    for _ in range(n):
        c, k = input().split()
        strs += c*int(k)

    print(f'#{t}')
    for i in range(0, len(strs), 10):
        print(strs[i:i+10])
