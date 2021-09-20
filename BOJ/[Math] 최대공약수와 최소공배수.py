from math import gcd

n, m = map(int, input().split())

print(gcd(n, m))
print(n*m//gcd(n, m))

# gcd 이용하지않고 푸는 방법
def gcd(n, m):
    # y가 0이 될 때까지 반복
    while m:
        n, m = m, n % m
        return n


# 9/20
from math import gcd

x, y = map(int, input().split())
print(gcd(x, y))
print(x*y//gcd(x, y))