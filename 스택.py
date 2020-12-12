import sys

N = int(sys.stdin.readline())
stack_list = []

for i in range(N):
    func = list(sys.stdin.readline().split())

    if func[0] == "push":
        stack_list.append(int(func[1]))

    elif func[0] == "pop":
        if not stack_list:
            print(-1)
        else:
            print(stack_list.pop())

    elif func[0] == "top":
        if not stack_list:
            print(-1)
        else:
            print(stack_list[-1])

    elif func[0] == "size":
        print(len(stack_list))

    else:
        if len(stack_list) == 0:
            print(1)
        else:
            print(0)