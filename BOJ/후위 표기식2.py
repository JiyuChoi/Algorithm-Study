import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()
nums = [0]*n
stack = []

for i in range(n):
    nums[i] = int(sys.stdin.readline())

for x in s:
    if x.isupper():
        stack.append(nums[ord(x)-ord('A')])
    else:
        if x == "+":
            stack.append(stack.pop(-2) + stack.pop(-1))
        elif x == "-":
            stack.append(stack.pop(-2) - stack.pop(-1))
        elif x == "*":
            stack.append(stack.pop(-2) * stack.pop(-1))
        elif x == "/":
            stack.append(stack.pop(-2) / stack.pop(-1))


print("%.2f" %stack[0])