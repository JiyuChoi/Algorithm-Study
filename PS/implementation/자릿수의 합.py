def digit_sum(x):
    return sum(list(map(int, str(x))))

n = int(input())
num = list(map(int, input().split()))
max_v = float("-inf")

for x in num:
    tot = digit_sum(x)
    if tot > max_v:
        max_v = tot
        res = x

print(res)