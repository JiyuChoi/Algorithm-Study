from collections import deque
import sys

input = sys.stdin.readline
n, k = map(int, input().split())
belt = deque(map(int, input().split()))

robot = deque([0]*(2*n))
cnt = 0

while True:
    cnt += 1
    belt.rotate(1)
    robot.rotate(1)
    robot[n-1] = 0

    for i in range(n-2, -1, -1):
        if belt[i+1] > 0 and robot[i] == 1 and robot[i+1] == 0:
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1
    robot[-1] = 0 # 내리는 위치에 도달한 로봇 즉시 내리기

    if belt[0] != 0:
        robot[0] = 1
        belt[0] -= 1

    if belt.count(0) >= k:
        break

print(cnt)
