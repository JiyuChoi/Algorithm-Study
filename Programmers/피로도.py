from itertools import permutations

def solution(k, dungeons):
    answer = 0
    l = len(dungeons)

    for pm in permutations(dungeons, l):
        cnt = 0
        e = k
        for p in pm:
            if e >= p[0]:
                e -= p[1]
                cnt += 1

        if cnt > answer:
            answer = cnt

    return answer