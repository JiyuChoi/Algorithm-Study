from collections import Counter

n = int(input())
word = [input() for _ in range(2*n-1)]

for key, value in Counter(word).items():
    if value == 1:
        print(key)
        break

# Counter의 기능 이용!
word = [input() for _ in range(n)]
using = [input() for _ in range(n-1)]

print(*list((Counter(word) - Counter(using)).keys()))

