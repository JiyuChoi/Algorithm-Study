s = list(input())
stack = []
answer = ""
for x in s:
    if x.isdigit():
        answer += x
    else:
        if x == "(":
            stack.append(x)
        elif x == "*" or x == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                answer += stack.pop()
            stack.append(x)
        elif x == "+" or x == "-":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.append(x)
        elif x == ")":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.pop()
            
for x in stack:
    answer += x

print(answer)
