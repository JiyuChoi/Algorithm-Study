pipe = input()
# 잘린 파이프 수
res = 0
# 막대기 개수
cut = 0
stack = [pipe[0]]

for p in pipe[1:]:
    if stack[-1] == "(":
        if p == "(":
            cut += 1
        else:
            res += cut
    else:
        if p == ")":
            cut -= 1
            res += 1
    stack.append(p)

print(res)