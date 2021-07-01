# from math import ceil
# def solution(progresses, speeds):
#     answer = []
#     days = [ceil((100-p)/s) for p, s in zip(progresses, speeds)]
#     prev = days[0]
#     cnt = 0
#     for x in days:
#         if x <= prev:
#             cnt += 1
#         else:
#             answer.append(cnt)
#             prev = x
#             cnt = 1
#     answer.append(cnt)
#     return answer

from math import ceil
def solution(progress, speeds):
    days = [ceil((100-p)/s) for p, s in zip(progress, speeds)]
    front = 0
    res = []
    for idx in range(len(days)):
        if days[front] < days[idx]:
            res.append(idx-front)
            front = idx
    res.append(len(days)-front)
    return res

print(solution([93, 20, 55], [1, 30, 5]))