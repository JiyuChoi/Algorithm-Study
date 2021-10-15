import sys
import heapq as hq

n = int(sys.stdin.readline())
h = []

for _ in range(n):
    number = int(sys.stdin.readline())

    if number == 0:
        if not h:
            print(0)
        else:
            print(hq.heappop(h))

    elif str(number).isdigit():
        hq.heappush(h, number)


# 10/15 보다 간결해진 코드!
import heapq as hq
import sys

h = []
n = int(sys.stdin.readline())
for _ in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        print(hq.heappop(h) if h else 0)
    else:
        hq.heappush(h, num)