def check(answer):
    # 구조물을 전부 검사하는 방식
    for x, y, a, in answer:
        if a == 0:
            if y == 0 or (x-1, y, 1) in answer or (x, y-1, 0) in answer or (x, y, 1) in answer:
                continue
            else:
                return False
        elif a == 1:
            if (x, y-1, 0) in answer or (x+1, y-1, 0) in answer or ((x-1, y, 1) in answer and (x+1, y, 1) in answer):
                continue
            else:
                return False
    return True

def solution(n, bulid_frame):
    answer = set()
    for frame in bulid_frame:
        x, y, a, b = frame
        if b == 1:
            # 구조물을 먼저 설치하고 맞지 않는다면 제거
            answer.add((x, y, a))
            if not check(answer):
                answer.remove((x, y, a))
        elif b == 0:
            # 구조물을 먼저 제거하고 맞지 않다면 추가
            answer.remove((x, y, a))
            if not check(answer):
                answer.add((x, y, a))

    answer = map(list, answer)
    return sorted(answer)

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))