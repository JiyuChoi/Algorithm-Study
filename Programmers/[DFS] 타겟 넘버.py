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