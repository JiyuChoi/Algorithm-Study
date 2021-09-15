import sys
n = int(sys.stdin.readline())
dot_list = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))

for dot in dot_list:
    print(*dot)