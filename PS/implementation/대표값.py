n = int(input())
num = list(map(int, input().split()))
avg = round(sum(num)/n)
max_value = float("inf")

for idx, x in enumerate(num):
    d = abs(x - avg)
    if d < max_value:
        max_value = d
        score = x
        res = idx+1
    if d == max_value:
        if x > score:
            score = x
            res = idx + 1

print(avg, res)