import heapq

def solution(scoville, K):
    answer = 0
    h = []

    for i in scoville:
        heapq.heappush(h, i)

    # 가장 작은 수가 K보다 작으면 수행
    while h[0] < K:
        one = heapq.heappop(h)
        two = heapq.heappop(h) * 2
        mix = one + two
        heapq.heappush(h, mix)
        answer += 1

        # 만약 힙의 길이가 1이고 가장 작은 수가 K보다 작으면
        # 더이상 스코빌 지수를 K이상으로 만들 수 없으므로
        if len(h) == 1 and h[0] < K:
            return -1
    return answer


''' 다른 사람 풀이 (좀 더 깔끔한 풀이!)
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
'''

''' 210313 풀이
import heapq as hq

def solution(scoville, K):
    h = []
    answer = 0
    for value in scoville:
        hq.heappush(h, value)

    while True:
        first = hq.heappop(h)
        if first >= K:
            return answer
        if not len(h):
            return -1
        second = hq.heappop(h)
        mixed = first + second * 2
        hq.heappush(h, mixed)
        answer += 1
'''