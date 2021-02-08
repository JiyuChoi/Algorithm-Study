from collections import Counter
import sys

n = int(sys.stdin.readline())
number = [int(sys.stdin.readline()) for _ in range(n)]
number.sort()

# 산술평균
total = round(sum(number)/n)

# 중앙값
middle = number[n//2]

# 최빈값
if n > 1:
    value = Counter(number).most_common(2)
    if value[0][1] == value[1][1]:
        max_v = value[1][0]
    else:
        max_v = value[0][0]
else:
    max_v = number[0]

#범위
range = number[-1] - number[0]

print(total)
print(middle)
print(max_v)
print(range)