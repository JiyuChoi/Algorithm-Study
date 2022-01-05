import re

def solution(dartResult):
    answer = []
    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = {'#': -1, '*': 2, '': 1}

    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)

    for i in range(3):
        s, b, o = dart[i]
        if o == "*" and i > 0:
            answer[i - 1] *= 2
        answer.append(int(s) ** bonus[b] * option[o])

    return sum(answer)