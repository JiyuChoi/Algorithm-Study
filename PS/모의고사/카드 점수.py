def solution(nums, k):
    tot = sum(nums)
    remain = len(nums) - k

    window_sum = sum(nums[:remain])
    answer = window_sum

    for i in range(remain, len(nums)):
        window_sum += (nums[i] - nums[i-remain])
        answer = min(window_sum, answer)

    return tot - answer

print(solution([3, 2, 5, 6, 7, 1], 3))
