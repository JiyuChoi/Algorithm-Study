# def solution(n):
#     dp = [0]*(n+1)
#     dp[1] = 1
#
#     for i in range(2, n+1):
#         dp[i] = dp[i - 1] + 1
#         if i % 2 == 0:
#             dp[i] = min(dp[i-i//2] + 1, dp[i])
#         if i % 3 == 0:
#             dp[i] = min(dp[i-i//3*2] + 1, dp[i])
#
#     return dp[-1]
#
# print(solution(1900000000))


from collections import deque
import collections
def solution(n):
    ch = collections.defaultdict(int)
    Q = deque()
    Q.append(n)
    ch[n] = 1
    L = 0

    while(Q):
        length = len(Q)
        for i in range(length):
            x = Q.popleft()
            if x == 0:
                return L
            if ch[x-1] == 0:
                ch[x-1] = 1
                Q.append(x-1)
            if x % 2 == 0 and ch[x//2] == 0:
                ch[x//2] = 1
                Q.append(x//2)
            if x % 3 == 0 and ch[x//3] == 0:
                ch[x//3] = 1
                Q.append(x//3)
        L += 1

print(solution(10)) #30