from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque([(begin, answer)])
    visited = []

    while q:
        begin, answer = q.popleft()
        if begin == target:
            return answer

        for word in words:
            if word in visited:
                continue

            dif = 0
            for x, y in zip(begin, word):
                if x != y:
                    dif += 1

            if dif == 1:
                q.append((word, answer + 1))
                visited.append(word)

    return 0