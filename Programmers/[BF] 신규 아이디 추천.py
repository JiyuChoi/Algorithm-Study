new_id = "=.="

# def changedot(tmp):
#     answer = ''
#     for i in range(len(tmp)-1):
#         if tmp[i] == ".":
#             if tmp[i] != tmp[i + 1]:
#                 answer += "."
#         else:
#             answer += tmp[i]
#     answer += tmp[-1]
#     return answer


def solution(new_id):
    answer = ''

    # 1번
    new_id = new_id.lower()

    # 2번
    for x in new_id:
        if x in ["-", "_", "."] or x.islower() or x.isdecimal():
            answer += x

    # 3번
    # python스러운 풀이!
    while '..' in answer:
        answer = answer.replace('..', '.')
    # answer = changedot(answer)

    # 4번
    if answer:
        if answer[0] == ".":
            answer = answer[1:]

    if answer:
        if answer[-1] == ".":
            answer = answer[:-1]

    # 5번
    if not answer:
        answer += "a"

    # 6번
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    # 7번
    # 길이가 3보다 작은 경우 수행
    while len(answer) < 3:
        answer += answer[-1]

    return answer