def solution(N, stages):
    l = len(stages)
    fail = []
    for x in range(1, N+1):
        people = stages.count(x)
        fail.append((x, people/l) if l else (x, 0))
        l -= people
    fail.sort(key=lambda x: -x[1])

    answer = [f[0] for f in fail]
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))

