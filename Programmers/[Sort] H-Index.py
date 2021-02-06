def solution(citations):
    new = []
    citations.sort()
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i: #논문 인용횟수 >= 인용된 논문의 개수
            return l-i
    return 0