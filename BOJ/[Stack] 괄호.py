# T = int(input())
# for _ in range(T):
#     cnt = 0
#     ps = input()
#     for j in ps:
#         if j == '(':
#             cnt += 1
#         else:
#             cnt -= 1
#         #닫는 개수가 더 많거나 VPS가 아닌 경우
#         if cnt < 0:
#             print("NO")
#             break
#     # 여는 개수와 닫는 개수가 같은 경우
#     if cnt == 0:
#         print("YES")
#     # 여는 개수가 더 많은 경우
#     elif cnt > 0:
#         print("NO")
#
# # 9/17
# n = int(input())
# for _ in range(n):
#     strings = input()
#     stack = []
#     for char in strings:
#         if char == "(":
#             stack.append(char)
#         elif char == ")":
#             if len(stack) != 0 and stack[-1] == "(":
#                 stack.pop()
#             else:
#                 stack.append(")")
#                 break
#     if len(stack) == 0:
#         print("YES")
#     else:
#         print("NO")

# 3/7
def isValid(arr):
    stack = []
    for x in arr:
        if x == ")" and stack:
            if stack.pop() != "(":
                return False
        else:
            stack.append(x)
    if stack:
        return False
    return True

n = int(input())

for _ in range(n):
    arr = input()
    if isValid(arr):
        print("YES")
    else:
        print("NO")