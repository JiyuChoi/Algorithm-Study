import math

def solution(progresses, speeds):
    answer = []
    days = [math.ceil((100-p)/s) for p, s in zip(progresses, speeds)]
    front = 0
    for idx in range(len(days)):
        if days[front] < days[idx]:
            answer.append(idx-front)
            front = idx
    answer.append(len(days)-front)
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]

print(solution(progresses, speeds))