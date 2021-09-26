import sys

r = 2000000
ch = [1, 1] + [0 for _ in range(r-1)]
primes = []
for i in range(2, r+1):
    if ch[i] == 1:
        primes.append(i)
        for j in range(i+i, r, i):
            ch[j] = False

def isPrime(n):
    if n > r:
        for prime in primes:
            if prime >= n:
                break
            elif n % prime == 0:
                return False
        return True
    else:
        return ch[n]

for _ in range(int(input())):
    a, b = map(int, sys.stdin.readline().split())
    s = a+b
    if s < 4:
        print("NO")
    elif s % 2 == 0:
        print("YES")
    else:
        if isPrime(s-2):
            print("YES")
        else:
            print("NO")