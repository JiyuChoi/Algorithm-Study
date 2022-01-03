from collections import deque


def check(s):
    dic = {"]": "[", "}": "{", ")": "("}
    stack = []
    for x in s:
        if x == "]" or x == "}" or x == ")":
            if not stack:
                return False
            else:
                if stack.pop() != dic[x]:
                    return False
        else:
            stack.append(x)
    return True


def solution(s):
    answer = 0
    q = deque(list(s))

    if len(s) % 2 != 0:
        return 0

    for _ in range(len(s)):
        if check(q):
            answer += 1
        q.rotate(-1)
    return answer