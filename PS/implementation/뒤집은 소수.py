def reverse(x):
    return int(str(x)[::-1])

def isPrime(x):
    # 1인 경우 False
    if x < 2:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False
    return True

n = int(input())
num = list(map(int, input().split()))

for x in num:
    rev_num = reverse(x)
    if isPrime(rev_num):
        print(rev_num, end=" ")