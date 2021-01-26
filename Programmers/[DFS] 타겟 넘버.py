# dfs함수를 함수 안에 넣어서(중첩함수) 풀이하면 numbers, target 매개변수로 하지 않아도 문제 해결

def solution(numbers, target):
    # 전역 변수
    global answer
    answer = 0

    def dfs(l, sum):
        # 전역 변수
        global answer
        if l == len(numbers):
            if sum == target:
                answer += 1

        else:
            dfs(l + 1, sum + numbers[l])
            dfs(l + 1, sum - numbers[l])

    dfs(0, 0)
    return answer


# 중청함수 사용하지 않고 풀이
answer = 0

def dfs(l, numbers, target, sum):
    global answer
    if l == len(numbers):
        if sum == target:
            answer += 1
    else:
        dfs(l + 1, numbers, target, sum + numbers[l])
        dfs(l + 1, numbers, target, sum - numbers[l])

def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    return answer