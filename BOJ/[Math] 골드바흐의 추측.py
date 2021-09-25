import sys
r = 1000000
ch = [0]*(r+1)
for i in range(2, int(r**0.5)+1):
    if ch[i] == 0:
        for j in range(i*2, r+1, i):
            ch[j] = 1

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    for i in range(3, r):
        if ch[i] == 0:
            if ch[n-i] == 0 and n-i > 2:
                print(f'{n} = {i} + {n-i}')
                break
    else:
        print("Goldbach's conjecture is wrong.")
