def balanced_index(p):
    cnt = 0
    for i in range(len(p)):
        if p[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i

def check_proper(p):
    cnt = 0
    for x in p:
        if x == "(":
            cnt += 1
        else:
            if cnt == 0:
                return False
            cnt -= 1
    # 올바른 괄호 문자열
    return True

def solution(p):
    answer = ""
    if p == "":
        return answer
    idx = balanced_index(p)
    u = p[:idx+1]
    v = p[idx+1:]
    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = "(" + solution(v) + ")"
        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == "(":
                u[i] = ")"
            else:
                u[i] = "("
        answer += "".join(u)
    return answer