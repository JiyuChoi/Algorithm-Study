def solution(nums, link, k):
    answer = 0
    l = len(nums)
    route = [[0]*l for _ in range(l)]
    ch = [0]*l

    for x, y, t in link:
        route[x][y] = t
        route[y][x] = t

    def dfs(v, time, sum):
        nonlocal answer
        if time < 0:
            return

        ch[v] += 1
        if ch[v] == 1:
            sum += nums[v]
        if v == 0:
            answer = max(answer, sum)
        for i in range(l):
            if route[v][i] != 0:
                dfs(i, time - route[v][i], sum)
        ch[v] -= 1

    dfs(0, k, 0)
    return answer


print(solution([5, 25, 10, 30], [[0, 1, 11], [1, 2, 15], [0, 3, 12]], 47))