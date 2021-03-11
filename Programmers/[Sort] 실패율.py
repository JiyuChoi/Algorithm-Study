# 딕셔너리 이용 풀이
def solution(N, stages):
    answer = {}
    l = len(stages)

    for i in range(1, N+1):
        if l != 0:
            answer[i] = stages.count(i)/l
            l -= stages.count(i)
        else:
            answer[i] = 0

    return sorted(answer, key=lambda x: -answer[x])


'''
print(solution(5, [2,1,2,6,2,4,3,3] ))
'''


# 리스트 이용 풀이
def solution(N, stages):
    fail = [0]*(N+1)
    l = len(stages)

    for i in range(0, N+1):
        num = stages.count(i)
        if l != 0:
            fail[i] = (i, num/l)
            l -= num
        else:
            fail[i] = (i, 0)

    fail = sorted(fail[1:], key=lambda x: -x[1])

    answer = [i[0] for i in fail]

    return answer