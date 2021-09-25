def isPrime(x):
    for i in range(2, int(n**0.5)+1):
        if num[i] == 0:
            for j in range(i*2, n+1, i):
                num[j] = 1

n = int(input())
num = [0]*(n+1)
isPrime(n)
prime = [i for i in range(2, n+1) if num[i] == 0]

s, e, res = 0, 0, 0
while e <= len(prime):
    tot = sum(prime[s:e])
    if tot == n:
        res += 1
        e += 1
    elif tot < n:
        e += 1
    else:
        s += 1
print(res)