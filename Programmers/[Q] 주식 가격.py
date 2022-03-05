from collections import deque

def solution(prices):
    answer = []
    q = deque(prices)

    while q:
        now = q.popleft()
        cnt = 0

        for next in q:
            cnt += 1
            if now > next:
                break

        answer.append(cnt)

    return answer