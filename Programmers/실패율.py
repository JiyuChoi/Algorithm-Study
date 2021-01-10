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