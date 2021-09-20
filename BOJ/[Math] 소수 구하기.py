m, n = map(int, input().split())
ch = [0]*(n+1)

for i in range(2, int(n**0.5)+1):
    if ch[i] == 0:
        for j in range(i*2, n+1, i):
            ch[j] = 1

for i in range(m, n+1):
    if ch[i] == 0 and i != 1:
        print(i)