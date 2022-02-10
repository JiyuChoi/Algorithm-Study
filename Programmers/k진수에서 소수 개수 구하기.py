import math

def convert(n, k):
    word = ''
    while n > 0:
        n, mod = divmod(n, k)
        word += str(mod)
    return word[::-1]

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    word = convert(n, k)
    # num = re.sub('0+', " ", rev_base).split(" ") 이게 더 걸림

    for x in word.split('0'):
        if len(x) > 0:
            if is_prime(int(x)):
                answer += 1

    return answer