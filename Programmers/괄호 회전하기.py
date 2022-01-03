from collections import deque


def check(s):
    stack = []
    for char in s:
        if char in ("(", "[", "{"):
            stack.append(char)
        else:
            if not stack:
                return False
            if char == ")" and stack.pop() != "(":
                return False
            if char == "}" and stack.pop() != "{":
                return False
            if char == "]" and stack.pop() != "[":
                return False
    if stack:
        return False
    else:
        return True


def solution(s):
    answer = 0
    q = deque(list(s))
    for _ in range(len(s)):
        if check(q):
            answer += 1
        q.rotate(-1)
    return answer