from collections import deque
import sys
import re
t = int(input())
for _ in range(t):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    arr = sys.stdin.readline().rstrip()[1:-1].split(",")
    d = deque(arr)

    r_flag = 0
    err = 0

    if n == 0:
        d = deque([])

    for x in p:
        if x == "R":
            r_flag = not r_flag
        elif x == "D":
            if len(d) == 0:
                err = 1
                break
            if r_flag:
                d.pop()
            else:
                d.popleft()

    if err == 1:
        print("error")
    else:
        if r_flag:
            d.reverse()
        print("["+','.join(d)+"]")
