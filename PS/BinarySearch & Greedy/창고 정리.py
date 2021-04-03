l = int(input())
box = list(map(int, input().split()))
m = int(input())

# m번 박스 이동 수행
for _ in range(m):
    max_value = float("-inf")
    min_value = float("inf")
    max_idx = min_idx = 0
    # 박스 높이 최대/최소 비교
    for i in range(l):
        if box[i] >= max_value:
            max_value = box[i]
            max_idx = i
        if box[i] <= min_value:
            min_value = box[i]
            min_idx = i
    # 최대/최소를 파악했다면 박스 이동
    box[max_idx] -= 1
    box[min_idx] += 1

# 최대 높이 - 최소 높이
print(max(box)-min(box))