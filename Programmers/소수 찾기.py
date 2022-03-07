import itertools

def prime_number(number):
    if number > 1:
        for f in range(2, number):
            if number % f == 0:
                return False
    else:
        return False
    return True

def solution(numbers):
    count = 0
    answer = []

    # set으로 하면 중복이 지워진다
    for i in range(1, len(numbers) + 1):
        a = list(map(''.join, itertools.permutations(list(numbers), i)))
        for j in a:
            answer.append(int(j))
    answer = set(answer)

    for k in answer:
        if prime_number(k):
            count += 1

    return count