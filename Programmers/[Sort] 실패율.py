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
    answer = []
    l = len(stages)

    for i in range(1, N+1):
        num = stages.count(i)

        # 실패율 계산
        if l != 0:
            answer.append(i, num/l)
            l -= num
        else:
            answer.append(i, 0)

    # 실패율이 높은 순으로 정렬
    answer = sorted(answer[1:], key=lambda x: -x[1])

    answer = [i[0] for i in answer]

    return answer