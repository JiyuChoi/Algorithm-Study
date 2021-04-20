def dfs(l, sum, day):
    global max_value
    if day > n:
        return
    if l == n:
        if sum > max_value:
            max_value = sum
    else:
        dfs(l+time[l], sum+pay[l], day+time[l])
        dfs(l+1, sum, day)

n = int(input())
time, pay = [], []
for _ in range(n):
    t, p = map(int, input().split())
    time.append(t)
    pay.append(p)

max_value = float("-inf")
dfs(0,0,0)
print(max_value)