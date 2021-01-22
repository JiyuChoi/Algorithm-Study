import sys
import heapq as hq

h = []
# n 입력 받기
n = int(sys.stdin.readline())
# card 입력 받기
card = [int(sys.stdin.readline()) for _ in range(n)]
res = 0

# card를 heapq에 push
for value in card:
    hq.heappush(h, value)

# heapq에 하나의 원소(비교횟수 합)만 남을 때까지
while len(h) != 1:
    # 첫번째 작은 수
    first = hq.heappop(h)
    # 두번째 작은 수
    second = hq.heappop(h)
    # 두 카드의 비교횟수 합
    card_sum = first + second
    # 다시 heapq에 삽입
    hq.heappush(h, card_sum)
    res += card_sum

print(res)
