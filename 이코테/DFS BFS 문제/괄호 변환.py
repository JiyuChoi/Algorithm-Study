def divided(w):
    cnt = 0
    for i in range(len(w)):
        if w[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return w[:i+1], w[i+1:]

def isRight(u):
    cnt = 0
    for i in range(len(u)):
        if u[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if u[i] == ")" and cnt < 0:
            return False
    return True

def solution(w):
    if w == "":
        return w

    u, v = divided(w)

    if isRight(u):
        res = u + solution(v)
    else:
        res = "(" + solution(v) + ")"
        for p in u[1:len(u) - 1]:
            if p == '(':
                res += ')'
            else:
                res += '('
    return res

print(solution(input()))