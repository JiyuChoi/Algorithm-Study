# 균형잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p):
    cnt = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == "(":
            cnt += 1
        else:
            cnt -= 1
        if cnt == 0:
            return i

# 올바른 문자열인지 판단
def check_proper(p):
    cnt = 0 # 왼쪽 괄호의 개수
    for x in p:
        if x == "(":
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0: # 쌍이 맞지 않는 경우 False 반환
                return False
    # 올바른 괄호 문자열일 경우 True
    return True

def solution(p):
    answer = ""
    if p == "":
        return answer
    idx = balanced_index(p)
    u = p[:idx+1]
    v = p[idx+1:]
    # u가 올바른 문자열일 경우
    if check_proper(u):
        answer = u + solution(v)
    # u가 올바른 문자열이 아닌 경우
    else:
        answer = "(" + solution(v) + ")"
        u = u[1:-1] # 첫번째 문자와 마지막 문자 제거
        for x in u:
            if x == "(":
                answer += ")"
            else:
                answer += "("
    return answer