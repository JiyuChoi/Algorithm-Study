def solution(price, money, count):
    answer = -1
    total = money - sum([price*i for i in range(1, count+1)])
    answer = abs(total) if total < 0 else 0
    return answer


def solution(price, money, count):
    answer = -1
    pay = 0
    for i in range(count):
        pay += (i+1)*price
    answer = pay - money
    return 0 if answer < 0 else answer