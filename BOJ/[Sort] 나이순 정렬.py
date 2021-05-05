import sys
input = sys.stdin.readline

n = int(input())
people = []

for i in range(n):
    people.append(list(input().split()))

# 첫번째 인자인 나이로만 정렬 (두번째 인자로는 정렬하지 않음)
people.sort(key=lambda x: int(x[0]))

for p in people:
    print(*p)

