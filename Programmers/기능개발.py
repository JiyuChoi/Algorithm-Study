from math import ceil
def solution(progresses, speeds):
    answer = []
    days = [ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    prev = days[0]
    cnt = 0
    for x in days:
        if x <= prev:
            cnt += 1
        else:
            answer.append(cnt)
            prev = x
            cnt = 1
    answer.append(cnt)
    return answer

print(solution([93, 20, 55], [1, 30, 5]))