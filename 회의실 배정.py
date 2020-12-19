import sys
n = int(input())

timetable = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key=lambda x: (x[1], x[0]))
end_time = 0
cnt = 0

for s, e in timetable:
    if s >= end_time:
        cnt += 1
        end_time = e

print(cnt)