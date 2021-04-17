n = input()

stack = []

for x in n:
    if x.isdecimal():
        stack.append(int(x))
    else:
        n1 = stack.pop()
        n2 = stack.pop()

        if x == "+":
            stack.append(n2 + n1)
        elif x == "-":
            stack.append(n2 - n1)
        elif x == "*":
            stack.append(n2 * n1)
        elif x == "/":
            stack.append(n2 / n1)

print(stack[0])