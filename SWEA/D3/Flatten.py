for t in range(10):
    n = int(input())
    boxes = list(map(int, input().split()))

    while n > 0:
        max_idx, min_idx = 0, 0
        max_value = float("-inf")
        min_value = float("inf")
        for idx, value in enumerate(boxes):
            if value > max_value:
                max_value = value
                max_idx = idx
            if value < min_value:
                min_value = value
                min_idx = idx
        boxes[max_idx] -= 1
        boxes[min_idx] += 1
        n -= 1
    print(f'#{t+1} {max(boxes)-min(boxes)}')