import sys

input = sys.stdin.readline

n = int(input())

n1, n2, n3 = map(int, input().split())
max_dp = [n1, n2, n3]
min_dp = [n1, n2, n3]

for i in range(1, n):
    n1, n2, n3 = map(int, input().split())
    for j in range(3):
        if j == 0:
            max_1 = max(max_dp[0], max_dp[1]) + n1
            min_1 = min(min_dp[0], min_dp[1]) + n1
        elif j == 1:
            max_2 = max(max_dp[0], max_dp[1], max_dp[2]) + n2
            min_2 = min(min_dp[0], min_dp[1], min_dp[2]) + n2
        else:
            max_3 = max(max_dp[1], max_dp[2]) + n3
            min_3 = min(min_dp[1], min_dp[2]) + n3
    max_dp = [max_1, max_2, max_3]
    min_dp = [min_1, min_2, min_3]

print(max(max_dp), min(min_dp))