n = int(input())
top = list(map(int, input().split()))

stack = []
res = []
for i in range(n):
    now = top[i]
    while stack:
        if now >= stack[-1][1]:
            stack.pop()
        else:
            res.append(stack[-1][0])
            break
    else:
        res.append(0)
    stack.append((i+1, now))

print(*res)
