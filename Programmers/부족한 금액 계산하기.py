def solution(price, money, count):
    answer = -1
    total = money - sum([price*i for i in range(1, count+1)])
    answer = abs(total) if total < 0 else 0
    return answer