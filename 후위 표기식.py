import sys
s = sys.stdin.readline()
stack = []
res = ''

for x in s:
    if x.isupper():
        res += x
    else:
        if x == '(':
            stack.append(x)

        elif x == '+' or x == '-':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.append(x)

        elif x == '*' or x == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                res += stack.pop()
            stack.append(x)

        elif x == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()

print(res)