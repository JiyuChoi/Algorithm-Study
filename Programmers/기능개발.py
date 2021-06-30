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
    days = []
    res = []
    for p, s in zip(progress, speeds):
        day = ceil((100-p)/s)
        days.append(day)
    prev = days[0]
    cnt = 0
    for d in days:
        if prev >= d:
            cnt += 1
        else:
            res.append(cnt)
            prev = d
            cnt = 1
    res.append(cnt)
    return res

print(solution([93, 20, 55], [1, 30, 5]))