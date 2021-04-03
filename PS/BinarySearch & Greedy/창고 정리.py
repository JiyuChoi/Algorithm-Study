l = int(input())
box = sorted(list(map(int, input().split())))
m = int(input())

# m번 박스 이동 수행
for _ in range(m):
    box[-1] -= 1
    box[0] += 1
    box.sort()

# 최대 높이 - 최소 높이
print(box[-1]-box[0])