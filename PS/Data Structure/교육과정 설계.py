order = list(input())
n = int(input())

for i in range(n):
    class_list = input()
    stack = []
    for x in class_list:
        if x in order:
            stack.append(x)

    if stack == order:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))